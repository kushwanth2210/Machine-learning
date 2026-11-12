"""
Simple LLM agent built with Google ADK.
"""

try:
    from google.adk.agents import LlmAgent
except ImportError as exc:
    raise SystemExit(
        "Google ADK is not installed. Install it with: pip install google-adk"
    ) from exc

root_agent = LlmAgent(
    name="simple_llm_agent",
    model="gemini-2.0-flash",
    description="A lightweight assistant for friendly chat and simple tasks.",
    instruction=(
        "You are a helpful assistant. Keep responses concise, friendly, and clear. "
        "Answer questions directly and avoid long explanations unless asked."
    ),
)

if __name__ == "__main__":
    print("Google ADK agent loaded successfully.")
    print(f"Agent name: {root_agent.name}")
    print(f"Model: {root_agent.model}")
