def find(st, count, ans, low, high, char):
    # print(st,low,high,"ss")
    if high - low == 0:
        if chr(char) == st[high]:
            ans.append(count)
        else:
            ans.append(count + 1)
    else:
        check = 0
        mid = (high + low) // 2
        for k in st[low:mid + 1]:
            if k != chr(char):
                check += 1
        find(st, count + check, ans, mid + 1, high, char + 1)
        check = 0
        for k in st[mid + 1:high + 1]:
            if k != chr(char):
                check += 1
        find(st, count + check, ans, low, mid, char + 1)


for i in range(int(input())):
    n = int(input())
    st = input()
    ans = []
    find(st, 0, ans, 0, n - 1, 97)
    print(min(ans))
