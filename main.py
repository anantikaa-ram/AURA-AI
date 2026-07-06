from agents.coordinator import chat

print("🤖 Welcome to AURA!")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("👋 Goodbye!")
        break

    reply = chat(user)

    print("\n🤖 AURA:")
    print(reply)
    print()