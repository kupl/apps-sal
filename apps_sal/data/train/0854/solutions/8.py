# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    
    s=list(set(lst))
    if len(s)==len(lst):
        print("prekrasnyy")
    else:
        print("ne krasivo")

