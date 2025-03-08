from agno.agent import Agent
from ai.agents.pdf_agent import pdf_agent
from ai.agents.web_agent import web_agent
from agno.models.groq import GroqChat

hybrid_agent = Agent(
    team=[pdf_agent, web_agent],
    model=GroqChat(id="deepseek-r1-distill-qwen-32b"),
    instructions=["Retrieve from PDF first. If insufficient, fetch from the web."],
    markdown=True,
)
