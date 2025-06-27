# 50A

m, n = map(int, input().split( ))

if m%2 == 0 and n%2 == 1:  # m par, n impar
    dominos = (m/2)*n
    print(int(dominos))

if m%2 == 0 and n%2 == 0:  # m par, n par
    dominos = (m/2)*n
    print(int(dominos))

if m%2 == 1 and n%2 == 1:  # m impar, n impar
    dominos = (m*n - 1)/2
    print(int(dominos))

if m%2 == 1 and n%2 == 0:  # m impar, n par
    dominos = (n/2)*m
    print(int(dominos))