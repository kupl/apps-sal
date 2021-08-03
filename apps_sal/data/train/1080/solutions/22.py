t = int(input())
for i in range(t):
    s = input()
    if len(set(s)) == 2:
        print("YES")
    else:
        print("NO")

    # long method
    # e=""
    # c=0
    # # if len(s)%2==0 and s[0]!=s[1]:
    # #     d=s[0:2]
    # #     for i in range(int(len(s)/2)):
    # #         d=s[2*i:2*(i+1)]
    # #         if i==0:
    # #             e=d
    # #     # e=s[len(s)-2:len(s)]
    # #         if str(d)==str(e):
    # #             c+=1
    # #             e=d
    # #     if c==int(len(s)/2):
    # #         print("YES")
    # #     elif len(s)==2:
    # #         print("YES")
    # #     else:
    # #         print("NO")
    # # else:
    # #     print("NO")
