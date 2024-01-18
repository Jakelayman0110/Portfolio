import random

"""
    * Class: Secure Programming
    * Author: Chase Durbin/Jacob Layman
    * Due: 12-01-2023
    * Notes: Change comments will be as a comment underneath the change
"""
"""

  * Class: 44-141 Computer Programming I
  * Author: Chase Durbin/Bishal Adhikari
  * Description: Create a password validator/generator that will check
  passwords for strength, and will generate strong passwords
  * Due: 10-21-2021
  * I pledge that I have completed the programming assignment independently.
  * I have not copied the code from a student or any source.
  * I have not given my code to any other student and will not share this code
  with anyone under any circumstances.
"""


def printOptions():
    print(
        """
        Press "e" if you would like to check a password.\n
        Press "g" if you would like to generate a password.\n
        Press "q" if you would like to quit.
        """
    )
    choice = input("Enter a command: ")
    return choice


# ---- new function ----


def pwChoices(choice):
    if choice.lower() not in ["e", "g", "q"]:
        return False
    else:
        return True


# ---- new function ----


def printCheckPass(reason):
    if reason == 0:
        print("Valid password")
    elif reason == 1:
        print("Invalid Password - invalid characters")
    elif reason == 2:
        print("Invalid Password - not enough digits")
    elif reason == 3:
        print("Invalid Password - too short")


# ---- new function ----


# checks if the password meets the requirements
def checkPass(pw):
    valid = False
    numbers = 0
    reason = 0
    # ---- added reason so that we don't have to print in the function ----
    # checks if the password meets the requirements
    if len(pw) >= 10:
        for i in pw:
            # check if the character is a number, calculates total numbers
            if ord(i) >= 48 and ord(i) <= 57:
                numbers += 1
            elif ord(i) >= 65 and ord(i) <= 90:  # checks uppercase letter
                valid = True
            elif ord(i) >= 97 and ord(i) <= 122:  # checks lowercase letter
                valid = True
            else:
                reason = 1
                # ---- reason 1 is invalid characters ----
                valid = False
                return reason
        if numbers >= 3 and valid:
            # ---- removed valid == True to simplify ----

            reason = 0
            # ---- reason 0 is valid ----
            return reason
        elif numbers < 3 and valid:
            # ---- removed valid == True to simplify ----

            reason = 2
            # ---- reason 2 is not enough digits ----
            return reason
    else:
        reason = 3
        # ---- reason 3 is too short ----
        return reason


# ---- new function ----


# generate password
def genPass(length):
    # gets a random character and adds it to the password
    pw = ""
    i = 0
    while i < length:
        # ---- changed for loop to while loop ----
        # creates a random number between 1-3
        randNum = random.randint(1, 3)
        # chooses a random letter(upper or lowercase) or a random number
        char = ""
        if randNum == 1:
            char = random.randint(48, 57)
            char = chr(char)
        elif randNum == 2:
            char = random.randint(65, 90)
            char = chr(char)
        elif randNum == 3:
            char = random.randint(97, 122)
            char = chr(char)
        # adds the random character to the string pw
        pw += str(char)
        i += 1
    while checkPass(pw) != 0:
        pw = genPass(length)
    return pw


# ---- new function ----


def main():
    # priming read
    choice = printOptions()
    while not pwChoices(choice):
        choice = printOptions()

    valid = True

    # while the user has not input q

    while choice.lower() != "q":
        if choice.lower() == "e" and valid:
            # ---- removed valid == True to simplify ----

            # get password input
            pw = input("Please type your password here: ")
            printCheckPass(checkPass(pw))
            # ---- added checkPass() ----
            # asks for input again
            valid = True
            choice = printOptions()
            while not pwChoices(choice):
                choice = printOptions()
            # generate password
        elif choice.lower() == "g" and valid:
            # ---- removed valid == True to simplify ----
            pw = ""
            length = input("Enter the length of password to generate: ")
            try:
                val = int(length)
                if val < 10:
                    print("please enter a length greater or equal to 10")
                    continue
                pw = genPass(val)
                checkPass(pw)
                print(pw)
            except ValueError:
                print("please enter a valid length")
                continue
            # checks that the password meets the requirements for a valid
            # password
            # ---- changed to use function ----
            # asks for input again
            valid = True
            # ---- using pwChoices function ----
            choice = printOptions()
            while not pwChoices(choice):
                choice = printOptions()
    print("\nThank you for using the password machine!")


if __name__ == "__main__":
    main()
