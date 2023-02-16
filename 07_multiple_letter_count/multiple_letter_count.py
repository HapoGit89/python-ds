def multiple_letter_count(phrase):
    phrase_count = {let: phrase.count(let) for let in phrase}
    return phrase_count
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """