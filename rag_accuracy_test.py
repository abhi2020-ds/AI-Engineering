from pathlib import Path
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.nvidia import NVIDIA
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.core.text_splitter import TokenTextSplitter

load_dotenv(dotenv_path=Path('.env'))

llm = NVIDIA(model='openai/gpt-oss-120b')
embedder = NVIDIAEmbedding(model='nvidia/nv-embedqa-e5-v5')
Settings.llm = llm
Settings.embed_model = embedder

docs = SimpleDirectoryReader('data').load_data()
text_splitter = TokenTextSplitter(chunk_size=150, chunk_overlap=30)
nodes = text_splitter.get_nodes_from_documents(docs)
index = VectorStoreIndex(nodes, embed_model=embedder)
query_engine = index.as_query_engine(similarity_top_k=7, response_mode='compact')

questions = [
    {
        'question': 'What are the main features of this project?',
        'keywords': ['VectorStoreIndex', 'TokenTextSplitter', 'NVIDIA', 'query engine']
    },
    {
        'question': 'How do I install and configure this project?',
        'keywords': ['uv sync --active', 'NVIDIA_API_KEY', '.env', 'pyproject.toml']
    },
    {
        'question': 'What dependencies are used for the RAG pipeline?',
        'keywords': ['langchain', 'llama-index-core', 'llama-index-embeddings-nvidia', 'python-dotenv']
    },
    {
        'question': 'How do I implement a Retrieval Augmented Generation system with Python?',
        'keywords': ['SimpleDirectoryReader', 'TokenTextSplitter', 'VectorStoreIndex', 'query engine']
    }
]

print('Running RAG accuracy test...')
results = []
for item in questions:
    q = item['question']
    expected = item['keywords']
    response = query_engine.query(q)
    text = str(response).lower()
    response_matches = [kw for kw in expected if kw.lower() in text]

    retrieved_nodes = query_engine.retrieve(q)
    retriever_text = ' '.join(str(node) for node in retrieved_nodes).lower()
    retrieved_matches = [kw for kw in expected if kw.lower() in retriever_text]

    pass_rate = len(set(response_matches + retrieved_matches)) / len(expected)
    print('\nQUESTION:', q)
    print('RESPONSE:', response)
    print('EXPECTED KEYWORDS:', expected)
    print('RESPONSE MATCHES:', response_matches)
    print('RETRIEVED NODE MATCHES:', retrieved_matches)
    print('PASS RATE:', f'{pass_rate:.2f}')
    results.append(pass_rate >= 0.5)

print('\nSUMMARY:')
print(f'Passed {sum(results)} / {len(results)} questions')
if all(results):
    print('Accuracy test passed')
else:
    print('Accuracy test failed: review returned content and retrieval settings')
