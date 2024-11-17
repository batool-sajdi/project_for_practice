import random
import json
import os
import time
from threading import Timer


class UrduLearningGame:
    def __init__(self):
        self.vocabulary = {
            "کتاب": "Book",
            "پانی": "Water",
            "درخت": "Tree",
            "سورج": "Sun",
            "چاند": "Moon",
        }
        self.sentence_parts = [
            ("کتاب", "پڑھ", "رہا", "ہوں"),
            ("میں", "پانی", "پیتا", "ہوں"),
            ("درخت", "اونچا", "ہے"),
        ]
        self.scores = {}
        self.load_scores()
        self.current_players = []

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

    def set_players(self):
        """Set the players for the current session."""
        num_players = int(input("Enter the number of players (1 or more): "))
        for i in range(1, num_players + 1):
            name = input(f"Enter Player {i}'s name: ").strip()
            if name not in self.scores:
                self.scores[name] = 0
            self.current_players.append(name)

    def display_title(self):
        """Display the game title."""
        print("\033[95m" + """
        *******************************************
        *   Urdu Learning Game - Enhanced Edition *
        *******************************************
        """ + "\033[0m")

    def main_menu(self):
        """Display the main menu."""
        print("\n1. Play Matching Game")
        print("2. Play Fill-in-the-Blank Game")
        print("3. Play Sentence-Building Game")
        print("4. View Leaderboard")
        print("5. Exit")

    def play_matching_game(self, player):
        """Play the matching game."""
        print(f"\n🔤 {player}'s Turn: Match the Urdu Word with its English Meaning:")
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
                self.scores[player] += 10
            else:
                print(f"\033[91m❌ Incorrect! The correct answer was {meaning}.\033[0m")
        except (ValueError, IndexError):
            print("\033[91m⚠️ Invalid choice. Try again!\033[0m")

    def play_fill_in_the_blank(self, player):
        """Play the fill-in-the-blank game."""
        print(f"\n🔡 {player}'s Turn: Complete the Urdu Word:")
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
            self.scores[player] += 10
        else:
            print(f"\033[91m❌ Incorrect! The correct word was {complete}.\033[0m")

    def play_sentence_building_game(self, player):
        """Play the sentence-building game."""
        print(f"\n📝 {player}'s Turn: Arrange the words to form a correct sentence:")
        sentence = random.choice(self.sentence_parts)
        shuffled = list(sentence)
        random.shuffle(shuffled)

        print(f"Words: {' '.join(shuffled)}")
        user_input = input("Enter the correct sentence: ").strip()

        if user_input == " ".join(sentence):
            print("\033[92m✅ Correct! Well done! 🎉\033[0m")
            self.scores[player] += 15
        else:
            print(f"\033[91m❌ Incorrect! The correct sentence was: {' '.join(sentence)}.\033[0m")

    def view_leaderboard(self):
        """Display the leaderboard."""
        print("\n🏆 Leaderboard:")
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        for rank, (player, score) in enumerate(sorted_scores, 1):
            print(f"{rank}. {player}: {score} points")

    def show_performance_summary(self):
        """Show a summary of the game session."""
        print("\n📊 Performance Summary:")
        for player in self.current_players:
            print(f"{player}: {self.scores[player]} points")

    def run(self):
        """Run the game loop."""
        self.display_title()
        self.set_players()

        while True:
            self.main_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                for player in self.current_players:
                    self.play_matching_game(player)
            elif choice == "2":
                for player in self.current_players:
                    self.play_fill_in_the_blank(player)
            elif choice == "3":
                for player in self.current_players:
                    self.play_sentence_building_game(player)
            elif choice == "4":
                self.view_leaderboard()
            elif choice == "5":
                print("\nSaving progress and exiting... Goodbye! 👋")
                self.show_performance_summary()
                self.save_scores()
                break
            else:
                print("\033[91m⚠️ Invalid choice. Please try again.\033[0m")


if __name__ == "__main__":
    game = UrduLearningGame()
    game.run()
