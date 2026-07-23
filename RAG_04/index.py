from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiceCharacterTextSplitter


pdf_path = Path(__file__).parent / "lecture 1.pdf"

# Load the file in python given Program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()


# Split the docs init smaller chunks
text_splitter = RecursiceCharacterTextSplitter(
    chunk_size=1000
    chunk_overlap=400
)

chunks = text_splitter.split.documents(documents=docs)

print(docs[12])

 

# page_content='Bitcoin: A Peer-to-Peer Electronic Cash System 
# • From: Satoshi Nakamoto <satoshi <at> vistomail .com> 
# Subject: Bitcoin P2P e-cash pap er
# Newsgroups: gmane.comp.encryption.general
# Date: Friday 31st October 2008 18:10:00 UTC 
# • “I've been working on a new electronic cash system
# that's full
# y peer-to-peer, with no trusted third party.” 
# 13' metadata={'producer': 'Adobe PDF Library 19.12.68', 'creator': 'Acrobat PDFMaker 19 for Word', 'creationdate': '2019-09-24T13:57:07-04:00', 'author': 'Gary Gensler', 'company': 'Microsoft', 'keywords': '', 'moddate': '2020-01-17T09:57:54-05:00', 'sourcemodified': 'D:20190924175654', 'subject': '', 'title': '15.S12 F18 Sessionn 1: Introduction', 'source': 'D:\\AI\\RAG_04\\lecture 1.pdf', 'total_pages': 43, 'page': 12, 'page_label': '13'}

# */