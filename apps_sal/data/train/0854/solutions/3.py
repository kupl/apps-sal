# cook your dish here
def check(arr,n):
    for a in range(len(arr)):
        if a<len(arr)-1:
            if arr[a]==arr[a+1]:
                return True
                break
    return False

def __starting_point():
    t=int(input())
    n=[]
    l=[]
    for j in range(t):
        n.append(int(input()))
        l.append(list(map(int,input().split())))
        l[j].sort(reverse=True)
    for k in range(t):
        res = check(l[k], n[k])
        if (res):
            print("ne krasivo")
        else:
            print("prekrasnyy")
__starting_point()
