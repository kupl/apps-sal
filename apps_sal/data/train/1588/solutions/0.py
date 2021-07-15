try:
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        arr = []
        obj = {}
        for i in range(n):
            x,y = input().split()
            y = int(y)
            arr.append([x, y])
            if y in obj: obj[y].append(x)
            else: obj[y] = [x]
        arr.sort(key = lambda i: i[1], reverse = True)
        while len(arr) and len(obj[arr[-1][1]]) > 1:
            arr.pop()
        if len(arr) == 0:
            print('Nobody wins.')
        else:
            print(arr.pop()[0])
except:
    pass
