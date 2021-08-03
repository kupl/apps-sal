evens = ['0', '2', '4', '6', '8']
for _ in range(int(input())):
    num = input()
    if(num[-1] in evens and num != "2"):
        print("YES")
    else:
        print("NO")
