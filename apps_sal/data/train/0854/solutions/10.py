for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    if len(b)!=len(a):
        print("ne krasivo")
    else:
        print("prekrasnyy")
