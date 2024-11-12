score = 0
high_score = 0
# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },
    {
        "question": "Which country won Eurovision in 2021?",
        "options": ["A) Ukraine", "B) France", "C) Italy", "D) Germany"],
        "answer": "C"
    },
    {
        "question": "Where was tea invented?",
        "options": ["A) England", "B) Japan", "C) USA", "D) China"],
        "answer": "D"
    },
    # Learners can add more questions here following the same structure
]
playing = True
valid_answers = ["A", "B", "C", "D"]

while (playing == True):
    # Loop through each question
    for question in quiz_questions:
        # Display the question and options
        asking = True
        print(question["question"])
        for option in question["options"]:
            print(option)

        while (asking == True):
            # Get the user's answer
            user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
            # Check if the answer is correct
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
                asking = False
            else:
                if user_answer in valid_answers:
                    print(f"Wrong! The correct answer was {question['answer']}.")
                    asking = False
                else:
                    print("invalid Input! Try again.")

    # Goodbye message
    if (score > high_score):
        high_score = score
        print("Thanks for playing the Pub Quiz! Your Score was:", score, "New High Score!")
    else:
        print("Thanks for playing the Pub Quiz! Your Score was:", score, "The High Score is:", high_score)

    if (input("Play again? (Y/N)").strip().upper() != "Y"):
        playing = False
    else:
        score = 0
