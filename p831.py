import math
import numpy as np

# Part (a): Sequence Element
class SequenceElement:
    def __init__(self, x, k):
        self.x = x
        self.k = k

    def compute(self):
        return ((-1)**(self.k + 1) * self.x**(2*self.k + 1)) / ((2*self.k - 1) * (2*self.k + 1))

# Part (b): Sum S
class SumS:
    def __init__(self, n):
        self.n = n

    def compute(self):
        return sum([((-1)**(i-1))/i for i in range(1, self.n + 1)])

# Part (c): Determinant of Order n
class Determinant:
    def __init__(self, n):
        self.n = n

    def compute(self):
        A = np.array([[2 if i == j else 1 if abs(i-j) == 1 else 0 for j in range(self.n)] for i in range(self.n)])
        return np.linalg.det(A)

class SumA:
    def __init__(self, n, a0, a1, b0, b1):
        self.n = n
        self.a = [a0, a1]
        self.b = [b0, b1]

    def compute(self):
        for k in range(2, self.n + 1):
            self.a.append(self.a[k-1] * self.a[k-2])
            self.b.append(self.b[k-1]**2 - self.b[k-2]**2)
        return sum([self.a[k]/self.b[k] for k in range(self.n + 1)])

# Part (e): Taylor Series for cos(x)
class TaylorCos:
    def __init__(self, x, epsilon):
        self.x = x
        self.epsilon = epsilon

    def compute(self):
        term = 1
        sum_cos = 1
        n = 1
        while abs(term) > self.epsilon:
            term = ((-1)**n * self.x**(2*n)) / math.factorial(2*n)
            sum_cos += term
            n += 1
        return sum_cos

# Example usage:
if __name__ == "__main__":
    # Part (a)
    x = 2
    k = 1
    seq_elem = SequenceElement(x, k)
    print(f"Element x_{k} = {seq_elem.compute()}")

    # Part (b)
    n = 5
    sum_s = SumS(n)
    print(f"Sum S_{n} = {sum_s.compute()}")
    def compute(self):
        return sum([((-1)**(i-1))/i for i in range(1, self.n + 1)])

# Part (c): Determinant of Order n
class Determinant:
    def __init__(self, n):
        self.n = n

    def compute(self):
        A = np.array([[2 if i == j else 1 if abs(i-j) == 1 else 0 for j in range(self.n)] for i in range(self.n)])
        return np.linalg.det(A)

# Part (d): Sum A
class SumA:
    def __init__(self, n, a0, a1, b0, b1):
        self.n = n
        self.a = [a0, a1]
        self.b = [b0, b1]

    def compute(self):
        for k in range(2, self.n + 1):
            self.a.append(self.a[k-1] * self.a[k-2])
            self.b.append(self.b[k-1]**2 - self.b[k-2]**2)
        return sum([self.a[k]/self.b[k] for k in range(self.n + 1)])

# Part (e): Taylor Series for cos(x)
class TaylorCos:
    def __init__(self, x, epsilon):
        self.x = x
        self.epsilon = epsilon

    def compute(self):
        term = 1
        sum_cos = 1
        n = 1
        while abs(term) > self.epsilon:
            term = ((-1)**n * self.x**(2*n)) / math.factorial(2*n)
            sum_cos += term
            n += 1
        return sum_cos

# Example usage:
if __name__ == "__main__":
    # Part (a)
    x = 2
    k = 1
    seq_elem = SequenceElement(x, k)
    print(f"Element x_{k} = {seq_elem.compute()}")

    # Part (b)
    n = 5
    sum_s = SumS(n)
    print(f"Sum S_{n} = {sum_s.compute()}")

    # Part (c)
    n = 3
    det = Determinant(n)
    print(f"Determinant of order {n} = {det.compute()}")

    # Part (d)
    n = 5
    a0, a1 = 1, 2
    b0, b1 = 5, 5
    sum_a = SumA(n, a0, a1, b0, b1)
    print(f"Sum of series for n={n} = {sum_a.compute()}")

    # Part (e)
    x = math.pi / 3
    epsilon = 0.001
    taylor_cos = TaylorCos(x, epsilon)
    print(f"cos({x}) using Taylor series = {taylor_cos.compute()}")


# Part (a): Sequence Element
# Аналітично обчислені перші кілька елементів послідовності для порівняння:
# x_1 = 2, k = 1: ((-1)**(1 + 1) * 2**(2*1 + 1)) / ((2*1 - 1) * (2*1 + 1)) = 2/3
# x_2 = 2, k = 2: ((-1)**(2 + 1) * 2**(2*2 + 1)) / ((2*2 - 1) * (2*2 + 1)) = -8/15
# x_3 = 2, k = 3: ((-1)**(3 + 1) * 2**(2*3 + 1)) / ((2*3 - 1) * (2*3 + 1)) = 32/35

# Part (b): Sum S
# Аналітично обчислені перші кілька елементів суми для порівняння:
# S_1 = 1/1 = 1
# S_2 = 1/1 - 1/2 = 1/2
# S_3 = 1/1 - 1/2 + 1/3 = 5/12

# Part (c): Determinant of Order n
# Аналітично обчислений детермінант порядку n=3 для порівняння:
# Determinant of order 3 = |[2 1 0]|
#                           |[1 2 1]|
#                           |[0 1 2]| = 3

# Part (d): Sum A
# Аналітично обчислені перші кілька елементів суми для порівняння:
# A_0 = 1, A_1 = 2, b_0 = 5, b_1 = 5
# A_2 = A_1 * A_0 / b_1 - b_0 = 2 * 1 / 5 - 5 = -9/5
# A_3 = A_2 * A_1 / b_2 - b_1 = -9/5 * 2 / 25 - 5 = -103/25

# Part (e): Taylor Series for cos(x)
# Аналітично обчислені перші кілька елементів ряду Тейлора для порівняння:
# cos(x) ≈ 1 - x^2/2! = 1 - (pi/3)^2/2 = 1 - pi^2/18
