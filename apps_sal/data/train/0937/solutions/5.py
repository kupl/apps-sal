# cook your dish here
l = ["C", "E", "S"]
for t in range(int(input())):
    a = input().upper()
    flag = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            flag = 1
            print("no")
            break
    if flag == 0:
        print("yes")
