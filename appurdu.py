import random
import time
from collections import defaultdict

# Vocabulary List
words = {
    "کتاب": "Book",
    "پانی": "Water",
    "درخت": "Tree",
    "سورج": "Sun",
    "چاند": "Moon"
}

# Achievements System
achievements = []

def display_title():
    """Display game title."""
    print("\033[95m" + """
    **********************************
    *   اردو سیکھنے کا زبردست کھیل   *
    **********************************
    """ + "\033[0m")

def display_menu():
    """Display the main menu."""
    print("\n1. Match Urdu Words")
    print("2. Fill in the Blank")
    print("3. View Leaderboard")
    print("4. Exit Game")

def match_words_game():
    """Play the Match Words game."""
    print("\n🔤 Match the Urdu Word with its English Meaning:")
    urdu_word, meaning = random.choice(list(words.items()))
    options = list(words.values())
    random.shuffle(options)

    print(f"\nاردو لفظ: {urdu_word}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("\nاپنا انتخاب درج کریں: "))
        if options[choice - 1] == meaning:
            print("\033[92m✅ Correct! Well done! 🎉\033[0m")
            achievements.append("Matched a Word!")
            return 1
        else:
            print(f"\033[91m❌ Wrong! The correct answer was {meaning}.\033[0m")
            return 0
    except (ValueError, IndexError):
        print("\033[91m⚠️ Invalid input. Try again!\033[0m")
        return 0

def fill_in_the_blank_game():
    """Play the Fill in the Blank game."""
    print("\n🔡 Complete the Urdu Word:")
    incomplete, complete = random.choice([("ک_تاب", "کتاب"), ("پ_نی", "پانی"), ("در_خت", "درخت")])
    print(f"\nنامکمل لفظ: {incomplete}")

    user_input = input("لفظ مکمل کریں: ")
    if user_input == complete:
        print("\033[92m✅ Correct! Well done! 🎉\033[0m")
        achievements.append("Completed a Word!")
        return 1
    else:
        print(f"\033[91m❌ Wrong! The correct word was {complete}.\033[0m")
        return 0

def view_leaderboard(scores):
    """Display the leaderboard."""
    print("\n🏆 Leaderboard:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

def main():
    """Main function to run the game."""
    display_title()
    scores = defaultdict(int)

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            scores["Player"] += match_words_game()
        elif choice == "2":
            scores["Player"] += fill_in_the_blank_game()
        elif choice == "3":
            view_leaderboard(scores)
        elif choice == "4":
            print("\nThanks for playing! 🎉")
            break
        else:
            print("\033[91m⚠️ Invalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main()
