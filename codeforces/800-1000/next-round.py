# 158A
 
n, k = map(int, input().split( ))
pontuacao = list(map(int, input().split( )))
 
i = k
next_round = k
if pontuacao[0] == 0:
    print(0)
else: 
    for pontuacao[i] in pontuacao[i:]:
        if pontuacao[i] == pontuacao[k-1]:
            next_round += 1
        else: 
            break
        i += 1
    print(next_round)

# PROBLEMA: Nos k primeiros numeros tiver m zeros, o código da WRONG_ANSWER