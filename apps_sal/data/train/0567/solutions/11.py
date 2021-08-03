for _ in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    possible = 'No'
    for i in range(N - 2):
        if array[i] == array[i + 1] and array[i] == array[i + 2]:
            possible = 'Yes'
            break

    print(possible)
