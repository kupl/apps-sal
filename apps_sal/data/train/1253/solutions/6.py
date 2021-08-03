try:
    for _ in range(int(input())):
        n = int(input())
        st = list(input())
        d = int(input())
        p = list(map(int, input().split()))

#         a=[]
#         a.append(st)
        s11 = []
        for i in range(n):
            if(st[i] == "1"):
                s11.append(i)
#         print(s11)
        for i in range(d):
            #             print(s11,"fi")
            st.insert(p[i] - 1 + i, "|")
            for j in range(len(s11)):
                if(s11[j] >= p[i] - 1 + i):
                    s11[j] += 1
#             print(s11,"mi")
            for j in range(len(s11)):
                if(s11[j] == 0):
                    if(st[1] == "0"):
                        st[1] = "1"
                        s11.append(1)
                elif(s11[j] == len(st) - 1):
                    if(st[-2] == "0"):
                        st[-2] = "1"
                        s11.append(len(st) - 2)
                else:
                    if(st[s11[j] - 1] == "0"):
                        st[s11[j] - 1] = "1"
                        s11.append(s11[j] - 1)
                    if(st[s11[j] + 1] == "0"):
                        st[s11[j] + 1] = "1"
                        s11.append(s11[j] + 1)

        print(len(set(s11)))


except:
    pass
