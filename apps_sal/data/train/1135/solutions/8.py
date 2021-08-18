test = int(input())
for t in range(test):
    n, k = list(map(int, input().strip().split()))
    numbers = []
    for i in range(n):
        numbers.append(i + 1)
    temp = numbers[k]
    numbers[k] = numbers[n - 1]
    numbers[n - 1] = temp
    answer = ' '
    for num in numbers:
        answer = answer + str(num) + ' '
    print(answer.strip())
