# 4 4.296 3 3.8 -2 1.8 2 2.8678 1
arr = [x for x in input().split()]
for i in range(int(arr[0])):
    ans = float(arr[1])*1.0*(10**int(arr[2]))
    print("{:.2f}".format(round(ans, 2)))
    del arr[1]
    del arr[1]

