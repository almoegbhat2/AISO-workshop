from my_agent.tools import calculator, read_pdf
from google.adk.agents import llm_agent

# stronger reasoning agent
reasoning_agent = llm_agent.Agent(
    model="gemini-2.5-flash",   # bigger model
    name="reasoner",
    description="Handles complex reasoning, logic puzzles, and language problems.",
    instruction="""
    Solve reasoning and language puzzles carefully.
    Extract rules first, then apply them step-by-step.
    Return only the final answer when requested.
    """,
    tools=[calculator],
    sub_agents=[],
)

# main cheap agent
root_agent = llm_agent.Agent(
    model="gemini-2.5-flash-lite",
    name="agent",
    description="A helpful assistant.",
    instruction="""
    You are a precise and reliable assistant.

    Rules:
    - Use the calculator tool only for arithmetic or numeric computation.
    - Never use the calculator for language, translation, grammar, logic, reading, or file-analysis tasks.
    - For language tasks, infer the rules carefully and apply them exactly.
    - If the user asks for only the final answer, return only the final answer.
    - Do not add explanations unless asked.
    - If a question depends on an attached PDF, use the read_pdf tool instead of saying you cannot access files.
    """,
    tools=[calculator, read_pdf],
    sub_agents=[reasoning_agent],
)