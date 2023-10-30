# Lista de números
numeros = [101, 202, 303, 404, 505]

# Lista de índices
indices = [0, 1, 2, 3, 4]

# Lista de strings formatadas
strings_formatadas = ["Número: {} na lista {}.".format(numeros[i], indices[i]) for i in range(len(numeros))]

# Imprimir a lista de strings formatadas
for string in strings_formatadas:
    print(string)
