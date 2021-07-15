def solve(x):
        if not x:
              return x
        b = int(str(int(str(x)[0]) -1) +''.join('9' for i in range(len(str(x))-1)))
        a = x-b
        return sum([int(i) for i in str(a)])+sum([int(i) for i in str(b)])
