#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program adds two numbers together


def main():
    # This program adds two numbers together

    # Input
    first_number = int(input("enter the first number: "))
    second_number = int(input("enter the second number: "))

    # Procces
    sum_ = first_number + second_number

    # Output
    print("")
    print("The sum of {} + {} = {}".format(first_number, second_number, sum_))


if __name__ == "__main__":
    main()
