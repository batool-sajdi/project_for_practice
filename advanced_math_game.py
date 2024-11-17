import random
import time
import json

# Global Variables
leaderboard = []

def save_leaderboard(name, score):
    """Save the leaderboard to a file."""
    leaderboard.append({"name": name, "score": score})
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file)

def load_leaderboard():
    """Load the leaderboard from a file."""
    global leaderboard
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

def generate_question(difficulty, category):
    """Generate a math question based on difficulty and category."""
    if difficulty == "Easy":
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "Medium":
        num1, num2 = random.randint(10, 50), random.randint(10, 50)
    else:  # Hard
        num1, num2 = random.randint(50, 100), random.randint(50, 100)

    if category == "Addition":
        operation = "+"
    elif category == "Subtraction":
        operation = "-"
    elif category == "Multiplication":
        operation = "*"
    elif category == "Division":
        operation = "/"
        num1 = num1 * num2  # Ensure divisible numbers
    else:  # Random
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "/" and num2 != 0:
            num1 = num1 * num2

    question = f"What is {num1} {operation} {num2}?"
    answer = eval(f"{num1} {operation} {num2}")
    return question, answer

def main():
    """Main game function."""
    load_leaderboard()

    print("🎮 Welcome to the Advanced Math Learning Game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's get started. 🎉\n")
    
    # Select difficulty
    difficulty = input("Choose difficulty (Easy, Medium, Hard): ").capitalize()
    category = input("Choose category (Addition, Subtraction, Multiplication, Division, Random): ").capitalize()

    total_questions = 15
    score = 0
    lifelines = 2

    for i in range(total_questions):
        question, answer = generate_question(difficulty, category)
        print(f"\n📋 Question {i + 1}/{total_questions}: {question}")
        
        start_time = time.time()
        try:
            user_answer = float(input("Your answer: "))
            time_taken = time.time() - start_time

            if user_answer == answer:
                print("✅ Correct! 🎉")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer was {answer}.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

        # Timer and lifeline features
        if time_taken > 10:
            print("⏱️ Time's up for this question!")
        
        if lifelines > 0 and input("Use a lifeline? (yes/no): ").lower() == "yes":
            lifelines -= 1
            print(f"Lifeline used! Remaining: {lifelines}")
            print(f"Hint: The answer is approximately {round(answer, 1)}.")

        print(f"🎯 Progress: {i + 1}/{total_questions}\n")

    print("\n🎉 Game Over! 🎉")
    print(f"Your score: {score}/{total_questions}")
    
    save_leaderboard(name, score)

    # Display leaderboard
    print("\n🏆 Leaderboard 🏆")
    for entry in sorted(leaderboard, key=lambda x: x["score"], reverse=True):
        print(f"{entry['name']}: {entry['score']} points")

    print("\nThank you for playing! 👋")

if __name__ == "__main__":
    main()
