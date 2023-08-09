import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from html_template import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    '''Extract text from pdfs'''
    text = ''

    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text

def get_text_chunks(raw_text):
    '''Get text chunks'''
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_conversation_chain(vector_store):
    '''Get conversation chain'''
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id='google/flan-t5-xxl', model_kwargs={'temperature':0.5, 'max_length': 512})
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )

    return conversation_chain
    

def get_vector_store(text_chunks):
    '''Get vector store'''
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl')
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def handle_user_input(user_question):
    '''Handle user input'''
    if st.session_state.conversation is None:
        st.session_state.conversation = get_conversation_chain()
    bot_response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = bot_response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title='Chat with multiple PDFs', page_icon=':shark:', layout='wide')

    st.write(css, unsafe_allow_html=True)

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = None

    st.title('Chat with multiple PDFs')
    st.header('hat with multiple PDFs')
    user_question = st.text_input("Ask a question about your documents")
    if user_question:
        handle_user_input(user_question)


    with st.sidebar:
        st.subheader('Your documents')
        pdf_docs = st.file_uploader('Upload your documents and click on Process', type=['pdf'], accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing your documents...'):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                
                # create vector store
                vector_store = get_vector_store(text_chunks)

                # create conversation chain
                st.session_state.conversation =get_conversation_chain(vector_store)
                
    

if __name__ == '__main__':
    main()