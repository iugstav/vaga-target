import math


def is_in_fibonacci_sequence(n):
    def is_perfect_square(x):
        r = int(math.sqrt(x))
        return r**2 == x

    # o número está na sequência se uma dessas expressões for um quadrado perfeito
    return is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4)


def get_fib_number(n):
    if n == 0:
        return 0

    # verifica se está na sequência. Se não estiver, então poupa a computação
    # da sequência
    if not is_in_fibonacci_sequence(n):
        return -1

    # algoritmo de fibonacci iterativo
    i = 1
    f = 0

    iteration = 2
    while 1:
        f = f + i
        i = f - i

        if f == n:
            break

        iteration = iteration + 1

    return iteration


number = int(input("informe seu número: "))

ret = get_fib_number(number)
if ret == -1:
    print("eita, seu número não está na sequência de Fibonacci")
else:
    print(f"seu número pertence à sequência e está na posição {ret} da sequência")
