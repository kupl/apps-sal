t = int(input())
for _ in range(t):
    k = int(input())
    count = 1
    for _ in range(k):
        output = ''
        for index in range(1, k + 1):
            output += str(count * 2)
            count += 1
        print(output)
