for _ in range(int(input())):
    a = int(input())
    lst1 = list(map(int, input().split()))
    b = int(input())
    lst2 = list(map(int, input().split()))
    j = i = 0
    while i < b:
        #         print(i)
        while j < a:
            if lst2[i] == lst1[j]:
                break
            j += 1
        if j == a:
            break
        i += 1
    if i == b and j - 1 <= a - 1:
        print("Yes")
    else:
        print('No')
