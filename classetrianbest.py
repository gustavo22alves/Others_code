class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        lados.sort()  # Ordena os lados em ordem crescente

        # Verifica se o triângulo é retângulo pelo Teorema de Pitágoras
        if lados[0]**2 + lados[1]**2 == lados[2]**2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        razao_a = self.a / triangulo.a
        razao_b = self.b / triangulo.b
        razao_c = self.c / triangulo.c

        # Verifica se as razões entre os lados são iguais
        if razao_a == razao_b == razao_c:
            return True
        else:
            return False