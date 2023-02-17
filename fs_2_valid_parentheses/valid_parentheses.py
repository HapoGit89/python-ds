def valid_parentheses(parens):
    if (parens.count("(") + parens.count(")")) %2  != 0:
        return False
    elif parens[0] == ")":
        return False
    else:
        return True
    
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """