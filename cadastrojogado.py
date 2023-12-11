def jogador_caro(nome_jogador,gols_feitos):
    return f'O jogador {nome_jogador.upper()} fez {gols_feitos} gols nesta temporada!'

nome = str(input('digite algum nome: \n'))
if len(nome) == 0:
    nome = '<desconhecido>'

gols = str(input('digite o numero de gols: \n'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(jogador_caro(nome,gols))
