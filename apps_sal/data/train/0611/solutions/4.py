# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    seti1 = set(arr)
    l = [arr[i - 1] for i in arr]
    seti2 = set(l)
    if len(seti1) <= len(seti2):
        print("Poor Chef")
    else:
        print("Truly Happy")
