# cook your dish here
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    arr.sort()
    flag = 0
    for j in range(len(arr) - 1):
        if arr[j] == arr[j + 1]:
            print('ne krasivo')
            flag = 1
            break
    if flag == 0:
        print('prekrasnyy')
