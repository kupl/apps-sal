def get_ans(ar, n):
    for i in range(n - 2):
        if ar[i] == ar[i + 1] == ar[i + 2]:
            return 'Yes'
    return 'No'


for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))

    print(get_ans(ar, n))
