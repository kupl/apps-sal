# cook your dish here
for _ in range(int(input())):
    num = int(input())
    arr = list(map(int, input().split()))
    if(num % 2) == 1 and arr[0] == 1:
        arr1 = list(reversed(arr))
        for i in range(((len(arr) - 1) // 2)):
            if arr[i] + 1 == arr1[i + 1]:
                flag = 0
            else:
                flag = 1
                print('no')
                break
        if flag == 0:
            print('yes')
    else:
        print('no')
