def check_square(arr,nn,mm):
    total = 0
    for dim in range (2,mm+1):
        for row in range(nn-dim+1):
            for col in range(mm-dim+1):
                if arr[row][col]== arr[row][col+dim-1]==arr[row+dim-1][col]==arr[row+dim-1][col+dim-1]:
                    total+=1
            
    return total

for _ in range(int(input())):
    n,m = map(int,input().split())
    garden = []
    for i in range(n):
        garden.append(input())
    if n==1 or m == 1:
        print(0)
    else:
        print(check_square(garden,n,m))
