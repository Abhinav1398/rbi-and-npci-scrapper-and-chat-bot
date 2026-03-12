from src.pipeline.chat_engine import ask

while True:

    role = input("\nRole (product / tech / compliance): ")
    query = input("Ask: ")

    if query == "exit":
        break

    answer = ask(query, role)

    print("\nAnswer:\n", answer)