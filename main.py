from gtesmall2 import gtesmall
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

# VECTOR CONVERSION

md_files_location = '/home/navin/arjo_llm/output_md_files/output_20240304143059.md'

# Read the content of the MD file
with open(md_files_location, 'r', encoding='utf-8') as file:
    md_content = file.read()

# Split the content into smaller chunks (adjust parameters as needed)
chunk_size = 1000
chunk_overlap = 100
chunks = [md_content[i:i+chunk_size] for i in range(0, len(md_content), chunk_size - chunk_overlap)]

# Initialize the TextSplitter and create a list of documents
text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

# Create a CustomDocument class with 'page_content' and 'metadata' attributes
class CustomDocument:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

# Create a list of CustomDocument instances
# In this example, metadata is set to an empty dictionary, adjust as needed
documents = [CustomDocument(chunk, {}) for chunk in chunks]

# CHROMA DB
# Initialize the Chroma client without 'persistence_dir'
db = Chroma.from_documents(
    documents,
    gtesmall()
)

# Get the content of the database
db_content = db.get_content()

# Print or inspect the content
print(db_content)
