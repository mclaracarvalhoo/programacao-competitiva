# 231A

n = int(input())
i = 1
certeza = 0
for i in range(n):
    a, b, c = map(int, input().split( ))
    i += 1
    if a + b + c > 1: 
        certeza += 1

print(certeza)