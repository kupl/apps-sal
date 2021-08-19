"""
def sdvig():
    tmp=A[2*n-1]
    for i in range(2*n-3,0,-2):
        A[i+2]=A[i]
    A[1]=tmp

def check():
    tmp=0
    for i in range(n):
        tmp+=A[i]
    low,high=tmp,tmp
    for i in range(2*n):
        tmp-=A[i]
        tmp+=A[(i+n)%(2*n)]
        if(tmp<low):
            low=tmp
        if(tmp>high):
            high=tmp
        if(high-low>1):
            return False
    else:
        return True
for kek in range(100):
    n=int(input())
    A=[int(i) for i in range(1,2*n+1)]
    for i in range(n):
        sdvig()
        if(check()):
            print('YES')
            for i in A:
                print(i,end=' ')
            quit()
    else:
        print('NO')
        quit()
"""


def sdvig():
    tmp = A[2 * (n // 2) + 1]
    for i in range(2 * (n // 2) + 2, 2 * n, 2):
        tArr.append(A[i + 1])
    for i in range(1, 2 * n - 2 * (n // 2), 2):
        A[i + 2 * (n // 2)] = A[i]
    A[2 * n - 1] = tmp
    for i in range(len(tArr)):
        A[i * 2 + 1] = tArr[i]


n = int(input())
A = [int(i) for i in range(1, 2 * n + 1)]
tArr = []
if n % 2:
    sdvig()
    print('YES')
    for i in A:
        print(i, end=' ')
else:
    print('NO')
