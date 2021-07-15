def func(lst):
    for i in lst:
        if i == 2:
            print(i^3, end=' ')
        else:
            print(i^2, end=' ')


n = int(input())
lst = list(map(int, input().split()))
func(lst)


