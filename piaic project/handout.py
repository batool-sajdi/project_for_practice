import random

def main():


#Welcome to the High-Low Game!
    print("Welcome to the High-Low Game!")

#--------------------------------
    print("--------------------------------")

    compoter_number = random.randint(0,100)

    user_number = int(input("enter your number"))
#The computer's number is 23

    print(f"compoter number is { compoter_number} ")
     
#Your number is 82
    print(f"user_number is {user_number}")
    if user_number > compoter_number:
        print("Your number is HIGHER than the computer's number!")
    elif user_number < compoter_number:
        print("Your number is LOWER than the computer's number!")
    else:
        print("Wow! Your number is EQUAL to the computer's number! It's a tie!")
# This provided line is required to call the main() function.
if __name__ == '__main__':
    main()