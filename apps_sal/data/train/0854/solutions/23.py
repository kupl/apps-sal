n = int(input())
for i in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    l.sort()
    a = set(l)
    if len(a) == len(l):
        print('prekrasnyy')
    else:
        print('ne krasivo')
