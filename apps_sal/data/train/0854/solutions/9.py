# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    arr = input()
    arr = arr.split()
    if len(arr) == len(set(arr)):
        print("prekrasnyy")
    else:
        print("ne krasivo")
    # print(len(arr), len(set(arr)))

    t -= 1
