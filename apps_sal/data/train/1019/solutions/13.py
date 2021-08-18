for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if(n % 2) == 1 and a[0] == 1:
        arr1 = list(reversed(a))
        for i in range(((len(a) - 1) // 2)):
            if a[i] + 1 == arr1[i + 1]:
                f = 0
            else:
                f = 1
                print('no')
                break
        if f == 0:
            print('yes')
    else:
        print('no')
