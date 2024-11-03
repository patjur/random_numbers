import random


def guess_the_number():
    """Draw a number from 1-100.

    Take number from user.

    Try until user gives a proper number.

    :rtype: int
    :return: given number as int
    """
    computer_number = random.randint(1, 100)

    while True:
        user_input = input("Guess the number: ")

        try:
            user_guess = int(user_input)
        except ValueError:
            print("It's not a number!")
            continue

        if user_guess < computer_number:
            print("Too small!")
        elif user_guess > computer_number:
            print("Too big!")
        else:
            print("You win!")
            break


if __name__ == "__main__":
    guess_the_number()