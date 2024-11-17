import random

# Constants
N_NUMBERS: int = 11  # Number of random numbers to generate
MIN_VALUE: int = 1   # Minimum value for random number
MAX_VALUE: int = 100 # Maximum value for random number

def main():
    """
    Generate and print 10 random numbers in the range 1 to 100.
    """
    for _ in range(N_NUMBERS):  # Loop 10 times
        value = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number
        print(value, end=" ")  # Print the number on the same line with a space
    
    print()  # Print a newline after the numbers

# This provided line is required to call the main() function.
if __name__ == '__main__':
    main()
