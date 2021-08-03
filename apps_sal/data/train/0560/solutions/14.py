def win(arr1, arr2, n):
    a = max(arr1)
    b = max(arr2)
    for ind in range(n):
        if arr1[ind] == a:
            index_a = ind
        if arr2[ind] == b:
            index_b = ind

    arr1[index_a] = 0
    arr2[index_b] = 0
    sum_a, sum_b = 0, 0
    for i in range(n):
        sum_a += arr1[i]
    for j in range(n):
        sum_b += arr2[j]

    if sum_a < sum_b:
        print("Alice")
    elif sum_a > sum_b:
        print("Bob")
    else:
        print("Draw")


t = int(input())
for tc in range(t):
    n = int(input())
    arr1 = [int(ele) for ele in input().split()]
    arr2 = [int(ele) for ele in input().split()]
    win(arr1, arr2, n)
