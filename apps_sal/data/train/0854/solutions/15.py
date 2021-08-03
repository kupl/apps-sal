for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("prekrasnyy") if(len(arr) == len(set(arr))) else print("ne krasivo")
