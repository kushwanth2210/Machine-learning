"""
Simple chatbot demo using Google ADK.
"""

try:
    from google.adk.agents import LlmAgent
except ImportError as exc:
    raise SystemExit(
        "Google ADK is not installed. Install it with: pip install google-adk"
    ) from exc


def build_chatbot() -> LlmAgent:
    return LlmAgent(
        name="simple_chatbot",
        model="gemini-2.0-flash",
        description="A small chatbot for basic conversation.",
        instruction=(
            "You are a polite and helpful chatbot. Respond naturally in short messages. "
            "If the user says exit or quit, end the conversation politely."
        ),
    )


def main():
    chatbot = build_chatbot()
    print("Simple ADK chatbot started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: Goodbye!")
            break

        print(f"Bot: Hello! I am a Google ADK chatbot using {chatbot.model}.")
        print(f"Bot: You said: {user_input}")
        print("Bot: Ask me anything else!")


if __name__ == "__main__":
    main()
