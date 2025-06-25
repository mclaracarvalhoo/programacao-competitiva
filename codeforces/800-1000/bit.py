# 282A - Bit++

n = int(input())
i = 1
x = 0
for i in range(n):
    comando = input()
    i += 1
    if '+' in comando:
        x += 1
    if '-' in comando:
        x -= 1

print(x)