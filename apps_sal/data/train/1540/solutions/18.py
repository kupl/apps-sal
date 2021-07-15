# cook your dish here
t=int(input())
for w in range(t):
    n=int(input())
    k=int(input())
    if k%n==0 and k>=n:
        print('YES')
    else:
        print('NO   ')
