n = int(input())
numbers = input().split()
num = [int(x) for x in numbers]

total = sum(num)
max_num = max(num)
rounds = int((total + n - 2) / (n - 1))
print(max(max_num, rounds))
