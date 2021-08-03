for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if(len(a) == len(set(a))):
        print("prekrasnyy")
    else:
        print("ne krasivo")
