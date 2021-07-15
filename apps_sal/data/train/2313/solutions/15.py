#d_n= [C_m+A_n*B_m] for m in range()
#A=[ ->> ]
#B=[ <<- ]

def intersection(p,q):
    return (q[1]-p[1])/(p[0]-q[0])

def tree_cutting(n,A,B):
    I=[[0,0] for _ in range(n)]
    C=[0 for _ in range(n)]
    
    C[0]=0
    I[0][0]=-float("inf")
    I[0][1]=float("inf")
    C[1]=C[0]+A[1]*B[0]
    hull=[[B[0],C[0]],[B[1],C[1]]]
    I[0][1]=intersection(hull[-1],hull[-2])
    I[1][0]=I[0][1]
    I[1][1]=float("inf")
    curr=1
    k=0
    for i in range(2,n):
        k=min(k,curr)-1
        while True:
            k+=1
            if I[k][0]<=A[i] and A[i]<=I[k][1]:
                j=k
                break
        C[i]=hull[k][1]+A[i]*hull[k][0]
        p=[B[i],C[i]]

        while intersection(p,hull[-2])<=intersection(hull[-1],hull[-2]):
            hull.pop()
            curr-=1
            if len(hull)<2: break
        if B[i]!=hull[-1][0]:
            hull.append(p)
            I[curr][1]=intersection(hull[-1],hull[-2])
            curr+=1
            I[curr][0]=intersection(hull[-1],hull[-2])
            I[curr][1]=+float("inf")
        else:
            I[curr][1]=+float("inf")
    return C[n-1]

def __starting_point():
    n=int(input())
    A=list(map(int,input().strip().split()))
    B=list(map(int,input().strip().split()))
    print(tree_cutting(n,A,B))
__starting_point()
