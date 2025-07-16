# 263A - Beautiful Matrix

linha1 = list(map(int, input().split( )))
linha2 = list(map(int, input().split( )))
linha3 = list(map(int, input().split( )))
linha4 = list(map(int, input().split( )))
linha5 = list(map(int, input().split( )))

jogadas = 0

for _ in linha1:
    if _ == 1:
        jogadas += 2
if linha1[0] == 1 or linha1[4] == 1:
    jogadas += 2
if linha1[1] == 1 or linha1[3] == 1:
    jogadas += 1

for _ in linha2:
    if _ == 1:
        jogadas += 1
if linha2[0] == 1 or linha2[4] == 1:
    jogadas += 2
if linha2[1] == 1 or linha2[3] == 1:
    jogadas += 1

for _ in linha3:
    if _ == 1:
        jogadas += 0
if linha3[0] == 1 or linha3[4] == 1:
    jogadas += 2
if linha3[1] == 1 or linha3[3] == 1:
    jogadas += 1

for _ in linha4:
    if _ == 1:
        jogadas += 1
if linha4[0] == 1 or linha4[4] == 1:
    jogadas += 2
if linha4[1] == 1 or linha4[3] == 1:
    jogadas += 1

for _ in linha5:
    if _ == 1:
        jogadas += 2
if linha5[0] == 1 or linha5[4] == 1:
    jogadas += 2
if linha5[1] == 1 or linha5[3] == 1:
    jogadas += 1

print(jogadas)