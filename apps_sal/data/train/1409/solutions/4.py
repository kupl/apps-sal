def bin_one(temp: int):
    n = temp
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    return count


t = int(input())
values = []
for _ in range(t):
    values.append(input())

for value in values:
    print(bin_one(int(value)))
