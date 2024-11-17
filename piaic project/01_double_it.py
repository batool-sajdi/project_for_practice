def main():
    curr_value: int = int(input("enter your number"))
    while curr_value < 100:

      curr_value = curr_value * 2
      print(curr_value)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


