dict1 = {0:98, 1:57, 2:31, 3:45, 4:46}
for _ in range(int(input().strip())):
    s = list(input().strip())
    ss = 0
    for i in range(len(s)):
        ss = ((ord(s[i])-65) + dict1[i])  
        print(chr((ss%26)+65),end="")
    print()
