import numpy as np
import threading

class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = np.zeros((linhas, colunas), dtype=int)

    def preencher(self):
        self.matriz = np.random.randint(-9, 10, size=(self.linhas, self.colunas))

    def __str__(self):
        return str(self.matriz)


def multiplicar_matrizes(m1, m2):
    if m1.colunas != m2.linhas:
        raise ValueError("Dimensões incompatíveis")
    
    res = Matriz(m1.linhas, m2.colunas)
    
    for i in range(res.linhas):
        for j in range(res.colunas):
            res.matriz[i][j] = np.dot(m1.matriz[i, :], m2.matriz[:, j])
    
    return res


def multiplicar_t_matrizes(m1, m2):
    if m1.colunas != m2.linhas:
        raise ValueError("Dimensões incompatíveis")
    
    res = Matriz(m1.linhas, m2.colunas)
    threads = []
    num_threads = 12  # Ajustado para 12 threads
    tamanho_bloco = res.linhas // num_threads
    
    def worker(inicio, fim):
        for i in range(inicio, fim):
            for j in range(res.colunas):
                res.matriz[i][j] = np.dot(m1.matriz[i, :], m2.matriz[:, j])
    
    for i in range(num_threads):  # Use a variável num_threads aqui
        inicio = i * tamanho_bloco
        fim = (i + 1) * tamanho_bloco if i != (num_threads - 1) else res.linhas
        thread = threading.Thread(target=worker, args=(inicio, fim))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    return res


def liberar_matrizes(*matrizes):
    for m in matrizes:
        del m
