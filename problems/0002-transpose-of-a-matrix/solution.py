def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n = len(a)
    m = len(a[0])

    new_arr = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_arr[j][i] = a[i][j]

    return new_arr

    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    pass