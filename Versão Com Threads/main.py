import time
from matrix import Matrix, multiply_matrices, multiply_t_matrices, free_matrices

def main():
    matrices = []

    A, Z, Y = Matrix(5, 5), Matrix(5, 5), Matrix(5, 5)
    Z.fill()
    Y.fill()
    start_time = time.time()
    A = multiply_t_matrices(Z, Y)
    end_time = time.time()
    print(f"Time taken for multiply_t_matrices (5x5): {end_time - start_time:.6f} secs")
    print(A)
    matrices.extend([A, Z, Y])

    B, W, X = Matrix(100, 100), Matrix(100, 100), Matrix(100, 100)
    W.fill()
    X.fill()
    start_time = time.time()
    B = multiply_t_matrices(W, X)
    end_time = time.time()
    print(f"Time taken for multiply_t_matrices (100x100): {end_time - start_time:.6f} secs")
    matrices.extend([B, W, X])

    C, U, V = Matrix(1000, 1000), Matrix(1000, 1000), Matrix(1000, 1000)
    U.fill()
    V.fill()
    start_time = time.time()
    C = multiply_t_matrices(U, V)
    end_time = time.time()
    print(f"Time taken for multiply_t_matrices (1000x1000): {end_time - start_time:.6f} secs")
    matrices.extend([C, U, V])

    D, S, T = Matrix(2000, 2000), Matrix(2000, 2000), Matrix(2000, 2000)
    S.fill()
    T.fill()
    start_time = time.time()
    D = multiply_t_matrices(S, T)
    end_time = time.time()
    print(f"Time taken for multiply_t_matrices (2000x2000): {end_time - start_time:.6f} secs")
    matrices.extend([D, S, T])

    E, Q, R = Matrix(3000, 3000), Matrix(3000, 3000), Matrix(3000, 3000)
    Q.fill()
    R.fill()
    start_time = time.time()
    E = multiply_t_matrices(Q, R)
    end_time = time.time()
    print(f"Time taken for multiply_t_matrices (3000x3000): {end_time - start_time:.6f} secs")
    matrices.extend([E, Q, R])

    free_matrices(*matrices)

if __name__ == "__main__":
    main()
