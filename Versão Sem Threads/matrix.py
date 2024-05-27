import numpy as np

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


def liberar_matrizes(*matrizes):
    for m in matrizes:
        del m
