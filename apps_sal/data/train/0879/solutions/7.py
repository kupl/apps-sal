# cook your dish here
summ = [0, 45, 40, 45, 40, 25, 40, 45, 40, 45, 0]
arr = []

for i in range(0, 10):
    curr = []
    for j in range(1, 11):
        mul = i * j
        rem = mul % 10
        curr.append(rem)
    arr.append(curr)

# print(arr)


for _ in range(int(input())):
    num, n = (int(x) for x in input().split())
    count = (num // (n * 10))
    ans = count * (summ[n % 10])
    rem = (num - count * (n * 10)) // (n)
    # print("rem",rem)
    c = 0
    for i in range(rem):
        # print(arr[n%10][i])
        s = n % 10
        # print("s",s)
        c += arr[s][i]
        # print(arr[s][i])
    # print(ans,c)
    print(ans + c)
