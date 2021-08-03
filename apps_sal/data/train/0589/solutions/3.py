# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    count = 0
    pre = 0
    ans = 0
    for val in range(len(s)):
        if s[val] == "#":
            # print(count,pre)
            if count > pre:
                # print(ans)
                ans += 1
                pre = count
                # count=0
            count = 0
        else:
            count += 1
    print(ans)

    # pos=s[0]
    # for k in range(len(s)-1):
    #     if s[k+1]=="#":
    #         pos=s[k+1]
    #     else:

    #         if counter
