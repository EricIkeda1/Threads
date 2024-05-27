import time
from matrix import Matriz, multiplicar_matrizes, liberar_matrizes

def main():
    matrizes = []

    A, Z, Y = Matriz(5, 5), Matriz(5, 5), Matriz(5, 5)
    Z.preencher()
    Y.preencher()
    start_time = time.time()
    A = multiplicar_matrizes(Z, Y)
    end_time = time.time()
    print(f"Tempo para multiplicar_matrizes (5x5): {end_time - start_time:.6f} seg")
    print(A)
    matrizes.extend([A, Z, Y])

    B, W, X = Matriz(100, 100), Matriz(100, 100), Matriz(100, 100)
    W.preencher()
    X.preencher()
    start_time = time.time()
    B = multiplicar_matrizes(W, X)
    end_time = time.time()
    print(f"Tempo para multiplicar_matrizes (100x100): {end_time - start_time:.6f} seg")
    matrizes.extend([B, W, X])

    C, U, V = Matriz(1000, 1000), Matriz(1000, 1000), Matriz(1000, 1000)
    U.preencher()
    V.preencher()
    start_time = time.time()
    C = multiplicar_matrizes(U, V)
    end_time = time.time()
    print(f"Tempo para multiplicar_matrizes (1000x1000): {end_time - start_time:.6f} seg")
    matrizes.extend([C, U, V])

    D, S, T = Matriz(2000, 2000), Matriz(2000, 2000), Matriz(2000, 2000)
    S.preencher()
    T.preencher()
    start_time = time.time()
    D = multiplicar_matrizes(S, T)
    end_time = time.time()
    print(f"Tempo para multiplicar_matrizes (2000x2000): {end_time - start_time:.6f} seg")
    matrizes.extend([D, S, T])

    E, Q, R = Matriz(3000, 3000), Matriz(3000, 3000), Matriz(3000, 3000)
    Q.preencher()
    R.preencher()
    start_time = time.time()
    E = multiplicar_matrizes(Q, R)
    end_time = time.time()
    print(f"Tempo para multiplicar_matrizes (3000x3000): {end_time - start_time:.6f} seg")
    matrizes.extend([E, Q, R])

    liberar_matrizes(*matrizes)

if __name__ == "__main__":
    main()
