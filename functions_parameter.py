#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This program uses user defined functions


def calculate_area(base, height):
    # calculate area

    # process
    area = (base * height)/2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width
    print("Welcome to the area triangle calculator.")
    print("")
    
    # input
    base_from_user_string = input("Enter the base of triangle (cm): ")
    try:
        base_from_user = float(base_from_user_string)
        height_from_user_string = input("Enter the height of triangle (cm): ")
        try:
            height_from_user = float(height_from_user_string)
            print("")
            #call functions
            calculate_area(base_from_user, height_from_user)
        except Exception:
            print("Wrong input. Try again.")
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
