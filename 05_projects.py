questions = [
    {
        "question": "Which planet in our solar system is known for its prominent rings?",
        "options": ["A) Mars", "B) Jupiter", "C) Saturn", "D) Neptune"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Ag", "B) Au", "C) Fe", "D) Hg"],
        "answer": "B"
    },
    {
        "question": "Which tech company created the iPhone?",
        "options": ["A) Microsoft", "B) Google", "C) Apple", "D) Samsung"],
        "answer": "C"
    },
    {
        "question": "How many bones are there in an adult human body?",
        "options": ["A) 186", "B) 206", "C) 216", "D) 296"],
        "answer": "B"
    },
    {
        "question": "Which ocean is the largest on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the hardest natural substance known on Earth?",
        "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
        "answer": "C"
    },
    {
        "question": "In coding, what does 'HTML' stand for?",
        "options": ["A) Hyper Text Markup Language", "B) High Tech Machine Language", "C) Hyper Link Management Line", "D) Home Tool Markup Language"],
        "answer": "A"
    },
    {
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "options": ["A) Horse", "B) Camel", "C) Elephant", "D) Donkey"],
        "answer": "B"
    },
    {
        "question": "What gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Who painted the famous 'Mona Lisa'?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
        "answer": "C"
    }
]


for q in questions:
    print(q["question"])
    print(q["options"])
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q["answer"]:
        print("Correct!\n")    
    else:
        print(f"Incorrect! The correct answer is {q['answer']}.\n")
    