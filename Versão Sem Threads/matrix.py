import numpy as np

class Matrix:
    def __init__(self, lines, cols):
        self.lines = lines
        self.cols = cols
        self.matrix = np.zeros((lines, cols), dtype=int)

    def fill(self):
        self.matrix = np.random.randint(-9, 10, size=(self.lines, self.cols))

    def __str__(self):
        return str(self.matrix)


def multiply_matrices(m1, m2):
    if m1.cols != m2.lines:
        raise ValueError("Incompatible dimensions")
    
    res = Matrix(m1.lines, m2.cols)
    
    for i in range(res.lines):
        for j in range(res.cols):
            res.matrix[i][j] = np.dot(m1.matrix[i, :], m2.matrix[:, j])
    
    return res


def free_matrices(*matrices):
    for m in matrices:
        del m

