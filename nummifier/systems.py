# -*- coding: utf-8 -*-
"""
    systems
    ~~~~~~~
    Numerological systems to be used when nummifying strings.

    qa_nummify_character(): Nummify the given character according to the QA
        system.
"""
import re
import string


def qa_nummify_character(character):
    """Returns the nummification of the given character. If the character has
    no valid nummification in the given system then a 0 is returned.

    Arguments:
        character(str): The character to be translated.

    Returns:
        int: The nummification of the given character.
    """
    if not len(character) == 1:
        return 0
    if not re.match(r'[0-9A-Za-z]', character):
        return 0

    # 0-9 map to 0-9
    if character.isdigit():
        return int(character)

    # A-Z map to 10-35
    mapping = dict(zip(string.ascii_uppercase, range(10, 36)))
    return mapping[character.upper()]
