import numpy as np
import threading

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


def multiply_t_matrices(m1, m2):
    if m1.cols != m2.lines:
        raise ValueError("Incompatible dimensions")
    
    res = Matrix(m1.lines, m2.cols)
    threads = []
    num_threads = 12  # Ajustado para 12 threads
    chunk_size = res.lines // num_threads
    
    def worker(start, end):
        for i in range(start, end):
            for j in range(res.cols):
                res.matrix[i][j] = np.dot(m1.matrix[i, :], m2.matrix[:, j])
    
    for i in range(num_threads):  # Use a variável num_threads aqui
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != (num_threads - 1) else res.lines
        thread = threading.Thread(target=worker, args=(start, end))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    return res


def free_matrices(*matrices):
    for m in matrices:
        del m
