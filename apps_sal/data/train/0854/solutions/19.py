t=int(input())
for i in range(t):
    l=int(input())
    se={int(j) for j in input().split(" ")}
    if(l==len(se)):
        print("prekrasnyy")
    else:
        print("ne krasivo")
