def bouncy_ratio(percent):
    #if percent < 0.1 or percent > 0.9: raise ValueError()
    def check(i):
        d = [int(x) for x in str(i)]
        up, down = False, False
        for k in range(1, len(d)):
            if d[k] > d[k-1]: up = True
            if d[k] < d[k-1]: down = True
        return up and down
    bouncy = 0.0
    for n in range(100, 100000):
        if check(n): bouncy += 1
        if bouncy / n >= percent: return n 

