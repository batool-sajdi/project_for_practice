import random
import time

def generate_question(difficulty):
    """Generate a random math question based on the difficulty level."""
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    
    if difficulty == "easy":
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "medium":
        num1, num2 = random.randint(10, 50), random.randint(1, 20)
    else:  # Hard
        num1, num2 = random.randint(50, 100), random.randint(10, 50)

    if operation == '/':
        num1 = num1 * num2  # Ensure divisibility for clean results

    question = f"What is {num1} {operation} {num2}?"
    answer = eval(f"{num1} {operation} {num2}")
    return question, answer, operation, num2

def main():
    """Run the advanced math game."""
    print("\n✨ Welcome to the Advanced Math Learning Game! ✨")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's get started!\n")

    # Choose difficulty
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}
    difficulty = difficulty_map.get(input("Enter your choice (1/2/3): "), "easy")
    print(f"Difficulty set to: {difficulty.capitalize()}.\n")

    total_questions = 15
    score = 0
    correct_count = 0
    incorrect_count = 0
    leaderboard_score = 0

    for i in range(total_questions):
        question, answer, operation, num2 = generate_question(difficulty)
        print(f"📋 Question {i + 1}/{total_questions}: {question}")

        # Timer
        start_time = time.time()
        hint_shown = False

        try:
            while True:
                remaining_time = 10 - (time.time() - start_time)
                if remaining_time <= 0:
                    print("\n⏰ Time's up! Moving to the next question.")
                    incorrect_count += 1
                    break

                print(f"⏳ You have {int(remaining_time)} seconds left.")
                user_input = input("Your answer: ")

                if user_input == "hint" and operation == "/":
                    print(f"Hint: The divisor is {num2}, so the answer is in the range {answer - 1} to {answer + 1}.")
                    hint_shown = True
                    continue

                user_answer = float(user_input)
                if user_answer == answer:
                    print("✅ Correct! 🎉 Great job!")
                    score += 1
                    correct_count += 1
                else:
                    print(f"❌ Oops! The correct answer was {answer}.")
                    incorrect_count += 1
                break
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
            incorrect_count += 1

        print("✨ Progress:", f"{i + 1}/{total_questions} questions completed.\n")

    # Check and update leaderboard
    if score > leaderboard_score:
        leaderboard_score = score
        print(f"🏆 New High Score! {score}/{total_questions} 🎉\n")

    # Final Results
    print("\n🎉 Game Over! 🎉")
    print(f"📊 {player_name}'s Final Score: {score}/{total_questions}")
    print(f"✅ Correct answers: {correct_count}")
    print(f"❌ Incorrect answers: {incorrect_count}")

    if score >= 12:
        print("🌟 Amazing work! You're a math genius! 🌟")
    elif score >= 8:
        print("👍 Good job! Keep practicing and you'll get even better!")
    else:
        print("💪 Don't worry! Practice makes perfect. Keep it up!")

    print(f"\n📜 Leaderboard Score: {leaderboard_score}")

if __name__ == "__main__":
    main()
