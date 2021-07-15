# cook your dish here
t = int(input())
for _ in range(t):
    p = input()
    flag = False
    z = ['0','2','4','6','8']
    for ele in p:
        # print(ele)
        if ele in z:
            print(1)
            flag = True
            break
    if flag == False:
        print(0)
