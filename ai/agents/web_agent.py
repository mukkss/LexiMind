from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

web_agent = Agent(
    model=Groq(id="deepseek-r1-distill-qwen-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Search the web only when activated.",
    markdown=True,
)
