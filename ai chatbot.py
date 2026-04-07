from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

print("AI Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)