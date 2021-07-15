J = int(input())

for i in range(J):
    x=int(input())
    A=[int(x) for x in input().split()]
    B=[int(x) for x in input().split()]
    if(max(A)>max(B) or max(B)>max(A)):
        print("YES")
    else:
        print("NO")

