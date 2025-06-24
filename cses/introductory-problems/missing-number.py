n = int(input())
nums = list(map(int, input().split()))

total = n * (n + 1) // 2 # Soma de 1 a n
print(total - sum(nums)) 