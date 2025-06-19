from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

# 1단계: 문서 로드 및 임베딩 저장
loader = TextLoader("docs.txt")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = splitter.split_documents(docs)

embedding = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(splits, embedding)
retriever = vectorstore.as_retriever()

# 2단계: RAG 체인 구성
llm = ChatOpenAI(temperature=0)
rag_chain = ConversationalRetrievalChain.from_llm(llm, retriever)

# 3단계: Agent 체인 구성
retriever_tool = Tool(
    name="document_retriever",
    func=retriever.get_relevant_documents,
    description="Fetch documents relevant to user question from the knowledge base."
)

agent = initialize_agent([retriever_tool], llm, agent_type="zero-shot-react-description", verbose=True)

# 4단계: 비교 질문 및 응답
questions = [
    "What are the key components of LangChain?",
    "How is context handled differently in rag versus chat agents?"
]

chat_history = []
for q in questions:
    print(f"\n[질문] {q}\n")
    
    rag_response = rag_chain.run({"question": q, "chat_history": chat_history})
    print(f"🔷 RAG 응답:\n{rag_response}")
    
    agent_response = agent.run(q)
    print(f"🟣 Agent 응답:\n{agent_response}")
    
    print("\n[분석]")
    print("RAG는 문서 기반 직접 응답 방식으로, context가 정확히 포함되었을 때 높은 신뢰성을 보입니다.")
    print("Agent는 retriever tool을 reasoning에 활용해 더 긴 응답과 도구 활용 기반 추론을 제공합니다.")
    print("문서 기반 정보 정리는 RAG가 유리하고, 외부 도구 활용이나 복합 질의는 Agent가 더 강력합니다.")

