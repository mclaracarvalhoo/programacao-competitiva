# 158A
 
n, k = map(int, input().split( ))
pontuacoes = list(map(int, input().split( )))

next_round = 0
for pontuacao in pontuacoes:
    if pontuacao >= pontuacoes[k-1] and pontuacao > 0:
        next_round += 1

print(next_round)

# Olhei a solução