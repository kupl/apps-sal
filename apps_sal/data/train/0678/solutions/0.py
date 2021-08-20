test_case = int(input())
while test_case:
    n_people = int(input())
    array = list(map(int, input().strip().split()))
    sums = [0 for i in range(n_people)]
    sums[0] = array[0]
    for i in range(1, n_people):
        sums[i] = sums[i - 1] + array[i]
    k = 1
    count = 0
    i = 0
    while k < n_people:
        k = k + sums[i]
        i = i + sums[i]
        count = count + 1
    print(count)
    test_case -= 1
