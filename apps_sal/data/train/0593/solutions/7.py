# cook your dish here
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    s = input()
    brr = list(map(chr, range(97, 123)))
    count = 0
    for j in range(len(brr)):
        if brr[j] in s:
            continue
        else:
            count += arr[j]
    print(count)
