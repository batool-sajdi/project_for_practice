import random

def generate_question():
    """Generate a random math question and return the question and answer."""
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Ensure no division by zero or decimal answers for simplicity
    if operation == '/':
        num1 = num1 * num2  # Makes num1 divisible by num2

    question = f"What is {num1} {operation} {num2}?"
    answer = eval(f"{num1} {operation} {num2}")
    return question, answer

def main():
    """Run the math game."""
    print("\n✨ Welcome to the Math Learning Game! ✨")
    print("Solve the problems below. There are 15 questions.\n")

    total_questions = 15
    score = 0
    correct_count = 0
    incorrect_count = 0

    for i in range(total_questions):
        question, answer = generate_question()
        print(f"📋 Question {i + 1}/{total_questions}: {question}")

        try:
            user_answer = float(input("Your answer: "))
            if user_answer == answer:
                print("✅ Correct! 🎉 Great job!")
                score += 1
                correct_count += 1
            else:
                print(f"❌ Oops! The correct answer was {answer}.")
                incorrect_count += 1
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
            incorrect_count += 1

        print("✨ Progress: ", f"{i + 1}/{total_questions} questions completed.\n")

    print("\n🎉 Game Over! 🎉")
    print(f"📊 Your final score: {score}/{total_questions}")
    print(f"✅ Correct answers: {correct_count}")
    print(f"❌ Incorrect answers: {incorrect_count}")
    
    if score >= 12:
        print("🌟 Amazing work! You're a math genius! 🌟")
    elif score >= 8:
        print("👍 Good job! Keep practicing and you'll get even better!")
    else:
        print("💪 Don't worry! Practice makes perfect. Keep it up!")

if __name__ == "__main__":
    main()
