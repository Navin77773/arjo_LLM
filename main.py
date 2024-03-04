from gtesmall2 import gtesmall
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

#VECTOR CONVERSION

md_files_location ="/home/navin/arjo_llm/output_md_files/output_20240304121240.md"
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents()

# CHROMA DB
# Set the path where you want to store the embeddings
db_path = "/path/to/your/database"

# Initialize the Chroma client with the specified path
db = Chroma.from_documents(
    documents,
    gtesmall(),
    persistence_dir=db_path
)

# Get the content of the database
db_content = db.get_content()

# Print or inspect the content
print(db_content)

