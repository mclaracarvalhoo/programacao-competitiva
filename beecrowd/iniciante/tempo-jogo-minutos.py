# 1047 - Tempo de Jogo com Minutos

hi, mi, hf, mf = map(int, input().split( ))

if hi == hf and mi == mf:
    print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else: 
    ci = hi * 60 + mi
    cf = hf * 60 + mf
    duracao = cf - ci
    print(f'O JOGO DUROU {duracao//60} HORA(S) E {duracao%60} MINUTO(S)')