n = int(input()) 
print(n, end='')

while n != 1: 
    if n%2 == 0: # n is even
        n = n//2
    else: # n is odd
        n = n*3 + 1
    print(f' {n}', end='')