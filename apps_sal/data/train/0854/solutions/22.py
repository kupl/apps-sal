t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    if len(l) == len(s):
        print('prekrasnyy')
    else:
        print('ne krasivo')
