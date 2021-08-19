# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    tmp = s.split(" ")
    if "not" in tmp:
        print("Real Fancy")
    else:
        print("regularly fancy")
