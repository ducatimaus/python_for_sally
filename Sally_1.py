#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Ayleen"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """

    print("")
    print("Hi Sally!")

    capName = str(
        input("Which Star Trek Captain is your favorite? Enter name here: "))

    if not capName:
        print("You must enter a valid name!")

    if capName in "James T. Kirk":
        print("That' quite classic, dude!")
    elif capName in "Jean Luc Picard":
        print("The gentleman type, huh?")
    elif capName in "Benjamin Sisko":
        print("Our honored emissary ... ^^")
    elif capName in "Kathryn Janeway":
        print("She's really got a stiff upper lip!")
    elif capName in "Jonathan Archer":
        print("Not the worst choice:')")
    elif capName in "Christopher Pike":
        print("Now were talkin' ...")
    elif capName in "General Martok":
        print("Martok, son of Urthog? Qapla'!")
    else:
        print(capName + " ... Who???")
    print("")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
