t= int(input())
result = []
    
def logic(arr,p1,p2):
    return sum(arr[p1-1:p2])
    

for i in range(0,t):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for x in range(0,q):
        p1,p2 = list(map(int,input().split()))        
        result.append(logic(arr,p1,p2))
    
for item in result:
    print(item)

