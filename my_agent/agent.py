from my_agent.tools import calculator

"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash-lite",
    name="agent",
    description="A helpful assistant.",
    instruction=(
        """
        You are a precise and reliable assistant.

        When answering questions:
        - Think step-by-step before producing the final answer.
        - If the question involves reasoning or calculations, use the calculator tool and explain reasoing.
        - Provide concise but complete answers.
        - If you are uncertain, say so instead of guessing.
        """
    ),
    tools=[calculator],
    sub_agents=[],
)
