try:
    cases = int(input())
    for _ in range(cases):
        l = ''
        m = input()
        for i in range(len(m)):
            l += str(int(m[i]) - 2)
        print(l)
except:
    pass
