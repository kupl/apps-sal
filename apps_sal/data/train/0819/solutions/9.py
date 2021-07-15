# cook your dish here
def gcd(a,b):
    if(a == 0):
        return b
    return gcd(b%a,a)

testcases = int(input())
while(testcases):
    testcases -= 1
    x,y = map(int,input().split())
    if(gcd(x,y) == 1):
        print('YES')
    else:
        print('NO')
