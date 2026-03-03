def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Shakespeare", "C) J.K. Rowling", "D) Mark Twain"],
            "answer": "B"
        },
        {
            "question": "Which is the largest mammal?",
            "options": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Hippopotamus"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
            "answer": "B"
        },
        {
            "question": "Which continent is known as the Dark Continent?",
            "options": ["A) Asia", "B) Africa", "C) Europe", "D) South America"],
            "answer": "B"
        },
        {
            "question": "Who is known as the father of computers?",
            "options": ["A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Steve Jobs"],
            "answer": "B"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Mercury", "B) Venus", "C) Earth", "D) Mars"],
            "answer": "A"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Indian Ocean", "B) Arctic Ocean", "C) Atlantic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Silver"],
            "answer": "B"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Pablo Picasso", "B) Vincent van Gogh", "C) Leonardo da Vinci", "D) Michelangelo"],
            "answer": "C"
        },
        {
            "question": "Which is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        },
        {
            "question": "Which language is used to create web pages?",
            "options": ["A) HTML", "B) C++", "C) Java", "D) Python"],
            "answer": "A"
        },
        {
            "question": "What is the capital city of Japan?",
            "options": ["A) Kyoto", "B) Osaka", "C) Tokyo", "D) Nagasaki"],
            "answer": "C"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["A) 1940", "B) 1945", "C) 1950", "D) 1939"],
            "answer": "B"
        },
        {
            "question": "Which organ in the human body purifies blood?",
            "options": ["A) Heart", "B) Liver", "C) Kidney", "D) Lungs"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the 'language of AI'?",
            "options": ["A) C", "B) Java", "C) Python", "D) Prolog"],
            "answer": "D"
        },
        {
            "question": "Which planet is known for its rings?",
            "options": ["A) Jupiter", "B) Neptune", "C) Saturn", "D) Uranus"],
            "answer": "C"
        }
    ]

    score = 0
    print("🎮 Welcome to the MCQ Quiz Game! 🎮")
    print("----------------------------------")

    # Manual counter for question number
    i = 1
    for q in questions:
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Keep asking until a valid input is given
        while True:
            user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("⚠️ Invalid choice! Please enter only A, B, C, or D.")

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}\n")

        i += 1  # increase question number

    print(f"Your final score is {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You got all answers right!")
    elif score >= 10:
        print("👍 Good job!")
    else:
        print("😢 Better luck next time!")

run_quiz()