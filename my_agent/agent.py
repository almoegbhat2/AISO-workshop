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

        Follow these rules:
        - First understand exactly what the user is asking.
        - For any arithmetic, calculation, exponent, division, square root, percentage, or other numeric computation, always use the calculator tool.
        - Never do math in your head or estimate when the calculator tool can be used.
        - For reasoning questions, think step by step before giving the answer.
        - If the user asks for only the final answer, return only the final answer with no extra explanation.
        - If an attached file or image is needed to answer, use the available information from it rather than guessing.
        - If you are uncertain, say so instead of inventing facts.
        - Be concise, but do not leave out necessary information.
        """
    ),
    tools=[calculator],
    sub_agents=[],
)
