def conta_letra_a(string):
    ocurrences = 0
    for c in string:
        if c == "a" or c == "A":
            ocurrences += 1

text = input("informe o seu texto: ")
print(f"seu texto possui {conta_letra_a(text)} ocorrências da letra 'a', sendo ela maiúscula ou minúscula")
