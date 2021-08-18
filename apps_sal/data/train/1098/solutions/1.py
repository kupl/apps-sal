test_case = int(input())
while test_case:
    n = int(input())
    array = list(map(int, input().strip().split()))

    array.sort(reverse=True)
    i = 0
    s = 0
    while(i < n):
        s += array[i]
        i += 2
    print(s)
    test_case -= 1
