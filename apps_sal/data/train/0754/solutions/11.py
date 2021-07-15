def solution(n):
    while(n):
        if((n%10)&1==0):
            return 1
        else:
            n=n//10
    return 0

for i in range(int(input())):
    n=int(input())
    print(solution(n))
