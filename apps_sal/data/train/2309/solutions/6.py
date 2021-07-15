'''
from random import randint

visited = [-1] * (2 * 10 ** 6 + 1)
t = int(input())
for i in range(t):
    n, A = int(input()), list(map(int, input().split()))
    A.sort()
    res = [1] * n
    v = 1
    cnt = 0
    while cnt < n:
        #v = randint(1, 10**6)
        if all(visited[a + v] != i for a in A):
            for a in A:
                visited[a + v] = i
            res[cnt] = v
            cnt += 1
        v += 1
    print("YES\n" + ' '.join(map(str,res)))
'''

t = int(input())

def check(arr,v,dic):
    for i in arr:
        if dic[i+v] == 1:
            return True
    return False


def check2(arr,v,dic):
    ok = False
    for i in arr:
        if dic[i+v] == 1:
            ok = True
            break
    return ok


def check3(arr,v,dic):
    return any(dic[a + v] == 1 for a in arr)


dic = [0]*2000005

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    brr = [1]*n
    cnt = 0
    i = 1
    flag = True
    tmp = {}
    while cnt < n:
        '''
        while check(arr,i,dic):
            i += 1
        brr[cnt] = i

        for v in arr:
            #if i+v>2e6:
            #    break
            dic[i+v] = 1
            tmp[i+v] = 1
        cnt += 1
        '''
        #while any(dic[a + i] != 0 for a in arr):
        #    i += 1

        #while check3(arr, i, dic):
        #    i += 1

        ok = True
        for a in arr:
            if dic[a + i] == 1:
                ok = False
                break

        if not ok:
            i += 1
            continue

        for a in arr:
            dic[a + i] = 1
            tmp[a + i] = 1
        brr[cnt] = i
        cnt += 1
        i += 1
    if flag:
        print("YES")
        print(" ".join(map(str,brr)))
    else:
        print("NO")
    for k in list(tmp.keys()):
        dic[k] = 0

