"""
This module implements the testing exercise of the Section 15 of the course.
"""

import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a genius!')
            return True
    else:
        print('Please enter a number between 1 and 10')
        return False


if __name__ == '__main__':
    answer_arg = random.randint(1, 10)

    while True:
        try:
            guess_arg = int(input('Guess a number 1~10:  '))
            if run_guess(guess_arg, answer_arg):
                break
        except ValueError:
            print('Please enter a number')
            continue
