def six(n):
    return(1 + (n - 1) % 6)


def f(numbers):
    return sum(list(map(six, numbers)))


t = int(input())
answers = list()
for _ in range(t):
    throw = int(input())
    array = list(map(int, input().split()))
    answers.append(f(array))

for answer in answers:
    print(answer)
