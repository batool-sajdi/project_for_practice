import random
import json
import os
import time


class UrduLearningGame:
    def __init__(self):
        self.vocabulary = {
            "کتاب": "Book",
            "پانی": "Water",
            "درخت": "Tree",
            "سورج": "Sun",
            "چاند": "Moon",
        }
        self.scores = {}
        self.load_scores()
        self.current_player = None

    def load_scores(self):
        """Load scores from a file if available."""
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                self.scores = json.load(f)
        else:
            self.scores = {}

    def save_scores(self):
        """Save scores to a file."""
        with open("scores.json", "w") as f:
            json.dump(self.scores, f)

    def set_player(self):
        """Set the current player."""
        self.current_player = input("Enter your name: ").strip()
        if self.current_player not in self.scores:
            self.scores[self.current_player] = 0

    def display_title(self):
        """Display the game title."""
        print("\033[95m" + """
        *******************************************
        *   Urdu Learning Game - Professional    *
        *******************************************
        """ + "\033[0m")

    def main_menu(self):
        """Display the main menu."""
        print("\n1. Play Matching Game")
        print("2. Play Fill-in-the-Blank Game")
        print("3. View Leaderboard")
        print("4. Exit")

    def play_matching_game(self):
        """Play the matching game."""
        print("\n🔤 Match the Urdu Word with its English Meaning:")
        urdu_word, meaning = random.choice(list(self.vocabulary.items()))
        options = list(self.vocabulary.values())
        random.shuffle(options)

        print(f"\nاردو لفظ: {urdu_word}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("\nChoose the correct meaning: "))
            if options[choice - 1] == meaning:
                print("\033[92m✅ Correct! Well done! 🎉\033[0m")
                self.scores[self.current_player] += 10
            else:
                print(f"\033[91m❌ Incorrect! The correct answer was {meaning}.\033[0m")
        except (ValueError, IndexError):
            print("\033[91m⚠️ Invalid choice. Try again!\033[0m")

    def play_fill_in_the_blank(self):
        """Play the fill-in-the-blank game."""
        print("\n🔡 Complete the Urdu Word:")
        words_with_blanks = [
            ("ک_تاب", "کتاب"),
            ("پ_نی", "پانی"),
            ("در_خت", "درخت"),
            ("سور_ج", "سورج"),
            ("چان_", "چاند"),
        ]
        incomplete, complete = random.choice(words_with_blanks)

        print(f"\nنامکمل لفظ: {incomplete}")
        user_input = input("لفظ مکمل کریں: ").strip()

        if user_input == complete:
            print("\033[92m✅ Correct! Well done! 🎉\033[0m")
            self.scores[self.current_player] += 10
        else:
            print(f"\033[91m❌ Incorrect! The correct word was {complete}.\033[0m")

    def view_leaderboard(self):
        """Display the leaderboard."""
        print("\n🏆 Leaderboard:")
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        for rank, (player, score) in enumerate(sorted_scores, 1):
            print(f"{rank}. {player}: {score} points")

    def run(self):
        """Run the game loop."""
        self.display_title()
        self.set_player()

        while True:
            self.main_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.play_matching_game()
            elif choice == "2":
                self.play_fill_in_the_blank()
            elif choice == "3":
                self.view_leaderboard()
            elif choice == "4":
                print("\nSaving progress and exiting... Goodbye! 👋")
                self.save_scores()
                break
            else:
                print("\033[91m⚠️ Invalid choice. Please try again.\033[0m")


if __name__ == "__main__":
    game = UrduLearningGame()
    game.run()
