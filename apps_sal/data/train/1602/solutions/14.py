# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    x = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    while(True):
        if arr[0] == 1:
            print("Impossible")
            break
        else:
            del arr[0:x]
            arr = [arr[i] - 1 for i in range(len(arr))]
            if arr == []:
                print("Possible")
                break
