from dotenv import load_dotenv

load_dotenv()

from unbowed_ai import Docs  # noqa: E402
from unbowed_ai.contrib import ZoteroDB  # noqa: E402

docs = Docs()
zotero = ZoteroDB(library_type="user")  # "group" if group library

for item in zotero.iterate(
    q="Object-oriented analysis and design with applications, third edition",
    qmode="everything",
    sort="date",
    direction="desc",
    limit=100,
):
    print("Adding", item.title)
    print(f"Pdf: {item.pdf} docname: {item.key}")
    docs.add(item.pdf, docname=item.key)

answer = docs.query("What is The Meaning of Modularity?")
print(answer.formatted_answer)
