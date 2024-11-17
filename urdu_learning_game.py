import random
import time
import os

# Urdu words and their meanings
urdu_words = {
    "کتاب": "Book",
    "پانی": "Water",
    "درخت": "Tree",
    "سورج": "Sun",
    "چاند": "Moon",
    "زمین": "Earth",
    "ہوا": "Air",
    "آگ": "Fire",
    "چائے": "Tea",
    "ستارہ": "Star"
}

def display_menu():
    """Display the game menu."""
    print("\n✨ خوش آمدید! اردو سیکھنے کا کھیل ✨")
    print("1. لفظوں کا مطلب تلاش کریں (Match Words)")
    print("2. لفظ مکمل کریں (Fill in the Blank)")
    print("3. ٹائم ٹرائل موڈ (Time Trial Mode)")
    print("4. سکور بورڈ دیکھیں (View Leaderboard)")
    print("5. کھیل ختم کریں (Exit)")

def match_words_game():
    """Match Urdu words with their English meanings."""
    word, meaning = random.choice(list(urdu_words.items()))
    options = list(urdu_words.values())
    random.shuffle(options)

    print(f"\nاردو لفظ: {word}")
    print("نیچے دیے گئے اختیارات میں سے صحیح مطلب چنیں:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("اپنا انتخاب درج کریں (Enter your choice): "))
        if options[choice - 1] == meaning:
            print("\033[92m✅ صحیح جواب! شاباش! 🎉\033[0m")
            return 1
        else:
            print(f"\033[91m❌ غلط جواب! صحیح مطلب: {meaning}.\033[0m")
            return 0
    except (ValueError, IndexError):
        print("\033[91m⚠️ غلط انتخاب! براہ کرم 1 سے 4 کے درمیان نمبر درج کریں۔\033[0m")
        return 0

def fill_in_the_blank_game():
    """Fill in missing letters in Urdu words."""
    words = {
        "ک_تاب": "کتاب",
        "پ_نی": "پانی",
        "در_خت": "درخت",
        "سور_ج": "سورج",
        "چان_": "چاند"
    }

    incomplete, complete = random.choice(list(words.items()))
    print(f"\nنامکمل لفظ: {incomplete}")
    user_input = input("لفظ مکمل کریں: ")

    if user_input == complete:
        print("\033[92m✅ صحیح جواب! شاباش! 🎉\033[0m")
        return 1
    else:
        print(f"\033[91m❌ غلط جواب! صحیح لفظ: {complete}.\033[0m")
        return 0

def time_trial_mode():
    """Play as many questions as possible in 60 seconds."""
    print("\n⏱️ ٹائم ٹرائل شروع کریں! آپ کے پاس 60 سیکنڈز ہیں۔")
    start_time = time.time()
    score = 0

    while time.time() - start_time < 60:
        score += match_words_game()

    print(f"\n⏰ وقت ختم! آپ کا سکور: {score}")
    return score

def view_leaderboard():
    """Display the leaderboard."""
    print("\n🏆 سکور بورڈ 🏆")
    try:
        with open("leaderboard.txt", "r") as file:
            scores = file.readlines()
            scores = [line.strip() for line in scores]
            for score in sorted(scores, key=lambda x: int(x.split(": ")[1]), reverse=True):
                print(score)
    except FileNotFoundError:
        print("سکور بورڈ خالی ہے۔ کھیل کر سکور بنائیں!")

def save_score(name, score):
    """Save the player's score."""
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score}\n")

def main():
    """Main function to run the game."""
    print("\n✨ اردو سیکھنے کا کھیل شروع کریں! ✨")
    score = 0

    while True:
        display_menu()
        choice = input("اپنا انتخاب درج کریں (Enter your choice): ")

        if choice == "1":
            print("\n🔤 لفظوں کا مطلب تلاش کریں")
            score += match_words_game()
        elif choice == "2":
            print("\n🔡 لفظ مکمل کریں")
            score += fill_in_the_blank_game()
        elif choice == "3":
            print("\n⏱️ ٹائم ٹرائل موڈ")
            score += time_trial_mode()
        elif choice == "4":
            view_leaderboard()
        elif choice == "5":
            name = input("\nاپنا نام درج کریں: ")
            save_score(name, score)
            print(f"📊 آپ کا سکور محفوظ ہو گیا: {score}")
            break
        else:
            print("\033[91m⚠️ غلط انتخاب! براہ کرم 1، 2، 3، 4 یا 5 درج کریں۔\033[0m")

if __name__ == "__main__":
    main()
import sys
sys.stdout.reconfigure(encoding='utf-8')
