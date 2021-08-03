try:
    def find(l):
        f = 0
        for i in range(len(l) - 1):
            if(l[i] == 'f' and l[i + 1] == 'f'):
                f += find(l[i + 1:])
                f += find(l[i + 2:])
                break
            if(l[i] == 'g' and l[i + 1] == 'g'):
                f += find(l[i + 1:])
                f += find(l[i + 2:])
                break
        if(f == 0):
            return f + 1
        return f
    l = list(input())
    if(l.count('c') > 0 or l.count('k') > 0):
        print("0")
    else:
        print(find(l))
except EOFError as e:
    pass
