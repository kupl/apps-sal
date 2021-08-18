
for _ in range(int(input())):
    n = int(input())
    arr = list(i for i in input())

    count = 0
    char = arr[0]
    for j in range(1, n):
        if(char == arr[j]):
            count += 1
        char = arr[j]

    print(count)
