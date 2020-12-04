#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a "Month" program.



def main():
    # This is the function to run "Month" program.

    # Input
    month = int(input("Enter a number between 1-12:"))
    print("")

    # Process & output
    if month == 1:
        print("January")
    elif month == 2:
        print("february")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("september")
    elif month == 10:
        print("october")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
    else:
        print("You are not enter a number between 1-12")


if __name__ == "__main__":
    main()
