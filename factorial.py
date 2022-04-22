#!/usr/bin/env python3

# created by: paterry.BJ
# created on: 2022-04-21
# this program shows the factorial of the number entered


def main():
    # this program shows the factorial of the number entered
    counter = 1
    sum = 1

    # input
    positive_number = input("Enter any positive integer please: ")
    print("\n", end="")

    # process of the factorial number & output of the factorial number
    try:
        positive_number_int = int(positive_number)

        if positive_number_int >= 0:
            while counter <= positive_number_int:
                sum = sum * (counter)
                counter = counter + 1
            print("The factorial of {0} is {1}"
                  .format(positive_number_int, sum))

        else:
            print("That was not a positive integer. Enter an integer"
                  " above 0.")
            print("\n", end="")
    except Exception:
        print("That was not an integer. Please enter an integer.")


if __name__ == "__main__":
    main()