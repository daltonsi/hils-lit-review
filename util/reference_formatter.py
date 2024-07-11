from pyzotero import zotero
import bibtexparser


library_id = '7850473'
library_type = 'user'
api_key = 'S1gVjSPo0PZc5CYSps6LC6BY'
collection_key = 'BEXGCHLP'#'35LLP9AB'


OUTPUT_DIR ='/Users/daltonsi/HILS/hils-lit-review/bibtex'

zot = zotero.Zotero(library_id, library_type, api_key)

# items = zot.top(limit=5)
# # we've retrieved the latest five top-level items in our library
# # we can print each item's item type and ID
# for item in items:
#     print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
# zot.add_parameters(format='bibtex', style='REPLACE: your own style')
# bib_db = zot.top()
# Retrieve all items in the specified collection



#
collections = zot.collections()

for collection in collections:
    print(f"Collection Name: {collection['data']['name']}")
    print(f"Collection ID: {collection['data']['key']}")
    print("----")


zot.add_parameters(format='bibtex')
bib_db = zot.everything(zot.collection_items(collection_key))
with open(f"{OUTPUT_DIR}/lr_references.bib", 'w') as bibtex_file:
    bibtexparser.dump(bib_db, bibtex_file)