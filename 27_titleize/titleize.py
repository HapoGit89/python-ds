def titleize(phrase):
    phrase = phrase.lower()
    phrase_list = list(phrase)
    phrase_list[0] = phrase_list[0].upper()
    i=0
    while (i < len(phrase_list)):
        if phrase_list[i-1] == ' ':
            phrase_list[i] = phrase_list[i].upper()
        i += 1
    return ''.join(phrase_list)



    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
