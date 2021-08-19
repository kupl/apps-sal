(N, Q) = map(int, input().split())
dic = {}
for i in range(N):
    (a, b) = input().split()
    dic[a] = b
for kk in range(Q):
    a = input().strip()
    ext = ''
    if '.' in a:
        ext = a.split('.')[-1]
        if ext in dic.keys():
            print(dic[ext])
        else:
            print('unknown')
    else:
        print('unknown')
