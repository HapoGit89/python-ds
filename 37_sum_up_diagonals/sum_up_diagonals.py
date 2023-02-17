def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    summe_1=0
    summe_2=0
    x=0
    y=0
    while x < len(matrix[0]):
        summe_1 += matrix[y][x]
        y +=1
        x +=1
    
    x -= 1
    y = 0
    while x >= 0:
        summe_2 += matrix[y][x]
        y += 1
        x -=1
    
    return summe_1+summe_2