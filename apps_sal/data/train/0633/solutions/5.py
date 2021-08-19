# cook your dish here
test = int(input())


def base_mountain(x):
    max = x[0]
    for mountain in x:
        if mountain > max:
            max = mountain
    return max


for t in range(test):
    numbers = int(input())
    mountains = []
    for j in range(numbers):
        a = int(input())
        mountains.append(a)

    print(base_mountain(mountains))
