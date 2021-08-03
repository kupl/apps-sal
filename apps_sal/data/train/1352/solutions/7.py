# your code goes here
t = int(input().strip())
while t:
    n = int(input().strip())
    li = list(map(int, input().strip().split()))
    di = {}
    for i in li:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    for key in sorted(di):
        print("%s: %s" % (key, di[key]))
    t -= 1
