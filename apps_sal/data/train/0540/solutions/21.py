'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import bisect
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    a = bisect.bisect(l, m)
    s = list(set(l[0:a]))
    if(len(s) == 0):
        if(m == 1):
            if(m in l):
                print(len(l) - l.count(m))
            else:
                print(n)
        else:
            print(-1)
    else:
        s.sort()
        a = s[len(s) - 1]
        if(s == list(range(1, a + 1))):
            if(m in l):
                print(len(l) - l.count(m))
            else:
                print(n)

        else:
            print(-1)
