print("Welcome to the python Quiz Game!")

Score = 0

questions = [
    ("What is the capital of India?", "delhi"),
    ("Which language are we learning?", "python"),
    ("What is 5 + 5?", "10"),
    ("Which keyword is used to define a function in Python?", "def"),
    ("Which symbol is used for comments in Python?", "#")
]

for question, answer in questions:
    user_answer = input(question + " ")

    if user_answer.lower() == answer:
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")
        print("Correct answer:", answer)

print("\n🎉 Quiz Completed!")
print("Your score:", Score, "/", len(questions))