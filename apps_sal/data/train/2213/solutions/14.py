for _ in range(int(input())):
    a,b,n=[int(i) for i in input().split()]
    n%=3
    arr=[a,b,a^b]
    print(arr[n])
