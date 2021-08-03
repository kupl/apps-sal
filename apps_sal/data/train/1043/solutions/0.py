test_case = int(input())
for w in range(test_case):
    n, k = map(int, input().split())
    l = list(map(str, input().split()))
    ans = []
    for q in range(k):
        l2 = list(map(str, input().split()))
        ans.extend(l2[1:])
    for i in l:
        if i in ans:
            print('YES', end=' ')
        else:
            print('NO', end=' ')
    print()  # cook your dish here
