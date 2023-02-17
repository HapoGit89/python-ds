def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_l = list(str(num1))
    num2_l = list(str(num2))
    for char in num1_l:
        if num1_l.count(char) != num2_l.count(char):
            return False
    for char in num2_l:
        if num1_l.count(char) != num2_l.count(char):
            return False
    return True
    