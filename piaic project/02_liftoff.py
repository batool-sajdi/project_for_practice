def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):  # Start at 10, go down to 1, decrement by 1
        print(i, end=" ")  # Print the number followed by a space, not a newline
    
    # Print "Liftoff!" after the countdown
    print("Liftoff!")

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()
