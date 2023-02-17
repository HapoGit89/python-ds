def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    summe = 0
    i1 = 0
    i2 = 1
    while i1 < len(nums):
        while i2 < len(nums):
            if nums[i2]>nums[i1]:
                summe +=1
            i2 += 1     
        i1 += 1
        i2 = i1 +1
    return summe