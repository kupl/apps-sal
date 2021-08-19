for _ in range(int(input())):
    N = int(input())
    l = [int(i) for i in input().split()]
    sum = 0
    for i in l:
        sum += i
    if sum % N == 0:
        avg = sum // N
    else:
        avg = sum // N + 1
    no_of_operations = avg * N - sum
    for i in l:
        if i > avg:
            no_of_operations += i - avg
        else:
            pass
    print(no_of_operations)
