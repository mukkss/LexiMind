from agno.agent import Agent
from agno.models.groq import Groq
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector
import os

db_url = os.getenv("SUPABASE_DB_URL")

pdf_knowledge = PDFUrlKnowledgeBase(
    urls=[],
    vector_db=PgVector(table_name="pdf_docs", db_url=db_url)
)

pdf_agent = Agent(
    model=Groq(id="deepseek-r1-distill-qwen-32b"),
    knowledge_base=pdf_knowledge,
    instructions="Retrieve from PDFs using RAG.",
    markdown=True,
)
