"""Brain games for hexlet code."""
#!/usr/bin/env python

from brain_games.cli import welcome_user


def main():
    """Brain games main function."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello,', name, '!')
