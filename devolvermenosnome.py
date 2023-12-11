nomes = ['ana', 'thiago','tadeuxdato','Ga']

def menor_nome(nomes):
    menor = nomes[0].strip()  # Remove espaços antes e depois do primeiro nome
    for nome in nomes:
        nome = nome.strip()  # Remove espaços antes e depois do nome atual
        if len(nome) < len(menor):
            menor = nome
    return menor.capitalize()  # Retorna o menor nome com a primeira letra maiúscula

print(menor_nome(nomes))