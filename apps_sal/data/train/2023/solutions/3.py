#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
    dprint('debug mode')
except ModuleNotFoundError:
    def dprint(*args, **kwargs):
        pass



inId = 0
outId = 0
if inId>0:
    dprint('use input', inId)
    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #标准输出重定向至文件
if outId>0:
    dprint('use output', outId)
    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #标准输出重定向至文件
    atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit
    
N, = getIntList()

for i in range(N+20):
    if i*i >N:
        break

x = i-1
if x*x !=N:
    x+=1
dprint(x)

t = N//x

res = []
for i in range(N- t*x):
    res.append(t*x+i+1)

for i in range(t-1,-1, -1):
    for j in range(x):
        res.append(i*x + j+1)

for x in res:
    print(x, end = ' ')








