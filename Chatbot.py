print("About Chat Box Project")
print("\U0001F916: \U0001F44B I am a ChatBox")

while True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("\U0001F916: Hii! How can I help you?")

    elif user == "how are you":
        print("\U0001F916: I am fine. Can you tell me your doubt?")

    elif user in ["can you tell about data structure", "can you tell about ds"]:
        print("\U0001F916: Data structure is a way of organizing and storing data.\n"
              "It is classified into two types:\n"
              "1. Linear data structures: linked list, stack, and queue\n"
              "2. Non-linear data structures: graphs and trees.")

    elif user == "bye":
        print("\U0001F916: Bye! Have a good day.")
        break

    else:
        print("\U0001F916: Sorry! I can't understand your words.")
