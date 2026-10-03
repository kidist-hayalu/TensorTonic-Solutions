import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    rows = len(A)
    cols = len(A[0])
    B = np.zeros((cols,rows))
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]

    return B