# 71A

n = int(input())
i = 1
for i in range(n):
    palavra = input()
    if len(palavra) > 10:
        print(f'{palavra[0]}{len(palavra)-2}{palavra[-1]}')
    else: 
        print(palavra)