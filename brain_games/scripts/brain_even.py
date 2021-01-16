"""This file release function even for hexlet code."""
import random

import prompt

from brain_games.cli import welcome_user


def correct_answer_is(number, user_answer):
    """Consctruct for correct answer.

    Parameters:
        number(int): This is programmed number.
        user_answer(str): User answer.
    """
    if (number % 2) == 0:
        print(
            '"',
            user_answer,
            '"is wrong answer ;(. Correct answer was "yes".',
            sep='',
        )
    elif (number % 2) == 1:
        print(
            '"',
            user_answer,
            '"is wrong answer ;(. Correct answer was "no".',
            sep='',
        )
    else:
        print('Unknow error')


def brain_even():
    """Construct for brain even.

    Returns:
        int: Answer correct or incorrect (1 or 0).
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    increment = 0
    while increment <= 2:
        number = random.randrange(0, 1000)
        print('Question:', str(number))
        user_answer = prompt.string('Answer: ')
        even = (number % 2 == 0 and user_answer == 'yes')
        odd = (number % 2 == 1 and user_answer == 'no')
        if even or odd:
            print('Correct!')
            increment += 1
            continue
        correct_answer_is(number, user_answer)
        return 0
    return 1


def main():
    """Brain even main function."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ', name, '!', sep='')
    even_result = brain_even()
    if even_result == 0:
        print('Lets try again ', name, '!', sep='')
    elif even_result == 1:
        print('Congratulations, ', name, '!', sep='')
