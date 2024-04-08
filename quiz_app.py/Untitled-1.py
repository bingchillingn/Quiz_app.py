



questions = [
       {
        "question": "What country has the highest life expectancy?",
        "options": ["A: India", "B: Somalia", "C: Hong kong", "D: Usa"],
        "answer": "C"
    },
    
       {
        "question": "What company was originally called Cadabra?",
        "options": ["A: Amazon", "B: Fodora", "C: Microsoft", "D: Google"],
        "answer": "A"
    },
    
       {
        "question": "Aureolin is a shade of what color?",
        "options": ["A: orange", "B: Yellow", "C: Red", "D: Purple"],
        "answer": "B"
    },
    
       {
        "question": "What country drinks the most coffee per capita?",
        "options": ["A: Sweden", "B: France", "C: Ukraine", "D: Finland"],
        "answer": "D"
    },
    
       {
        "question": "What sports car company manufactures the 911?",
        "options": ["A: Porsche", "B: Ford", "C: Bugatti", "D: Nissan"],
        "answer": "A"
    },
    
       {
        "question": "What Netflix show had the most streaming views in 2021?",
        "options": ["A: Squat Game", "B: Wednesday", "C: Squid Game", "D: France"],
        "answer": "C"
    },
    
         {
        "question": "Kratos is the main character of what video game series in 2021?",
        "options": ["A: Valorant", "B: Eldern ring", "C: God of War", "D: Fortnite"],
        "answer": "C"
    },
    
         {
        "question": "What is the largest Spanish-speaking city in the world?",
        "options": ["A: Madrid", "B: Africa", "C: Mexico City", "D: Brazil"],
        "answer": "C"
    },
    
         {
        "question": "What European country experienced the highest rate of population decline from 2015 - 2020?",
        "options": ["A: Bulgaria", "B: Norway", "C: China", "D: Lithuania"],
        "answer": "D"
    },
    
         {
        "question": "What country has the most islands?",
        "options": ["A: South africa", "B: Sweden", "C: Philippines", "D: Canada"],
        "answer": "B"
    },
    
         {
        "question": "What phone company produced the 3310?",
        "options": ["A: One Plus", "B: Nokia", "C: Samsung", "D: Iphone"],
        "answer": "B"
    },
    
         {
        "question": "What game studio makes the Red Dead Redemption series?",
        "options": ["A: Arab games", "B: Epic Games", "C: Riot Games", "D: Rockstar Games"],
        "answer": "D"
    },
    
         {
        "question": "What car manufacturer had the highest revenue in 2020?",
        "options": ["A: Ford", "B: Mercedes", "C: Volkswagen", "D: Toyota"],
        "answer": "C"
    },
    
         {
        "question": "How many countries are in Africa?",
        "options": ["A: 54", "B: 58", "C: 60", "D: 50"],
        "answer": "A"
    },
    
]

    # This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")
    
run_quiz(questions)
