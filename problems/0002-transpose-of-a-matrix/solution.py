def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    import numpy as np
    c=[]
    b=np.shape(a)
    for i in range (b[1]):
        d=[0]*b[0]
        c.append(d)
    

    for i in range (b[0]):
        for j in range (b[1]):
            c[j][i]=a[i][j]
    return c