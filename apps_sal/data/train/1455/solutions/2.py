n = eval(input())
grades = list(map(int, input().split()))

m = eval(input())
main = []
for df in range(m):
    x, y = list(map(int, input().split()))
    arr = []
    arr = grades[x - 1:y]
    arr.sort()
    sum = 0
    for nh in range(0, len(arr) - 1, 1):
        sum = sum + (arr[nh + 1] - arr[nh]) * (arr[nh + 1] - arr[nh])
    print(sum)
