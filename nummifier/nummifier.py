# -*- coding: utf-8 -*-
"""
    nummifier
    ~~~~~~~~~
    Contains common numerological operations.

    cumulate(): Cumulates the integers up to the given value.
    plex(): Computes the plex of the given number.
    nummify_string(): Calculate the nummification of the given string.
"""


def cumulate(up_to):
    """Add the integers from 0 up to the given number.

    Arguments:
        up_to(int): The number of sum up to

    Returns:
        int: The cumulation of the given number
    """
    return sum(range(up_to + 1))


def plex(initial_value):
    """Computes the plex of the given number. This is computed by adding the digits
    of the number to each other to produce a smaller number.

    Example:
    Plex(89) -> 8 + 9 = 17

    Arguments:
        initial_value(int): The initial value

    Returns:
        int: The plex of the given number
    """
    return sum([int(each) for each in str(initial_value)])


def nummify_string(s, nummifier):
    """Convert the given string into a series of numbers using the nummifier
    provided.

    Arguments:
        s(str): The string to be nummified.
        nummifier(function): The function to be used to nummify the string.

    Returns:
        list: List of the nummified form of the string.
    """
    return filter(None, [nummifier(each) for each in s])
