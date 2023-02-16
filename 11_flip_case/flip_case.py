def flip_case(phrase, to_swap):
    phrase_list = list(phrase)
    flipped_list = [x.lower() if x == to_swap and x.isupper() == True else x.upper() if x == to_swap else x for x in phrase_list]
    return ''.join(flipped_list)




    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
