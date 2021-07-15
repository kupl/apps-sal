q = int(input())
for i in range(q):
    n = int(input())
    a = input()
    b = input()
    countA = [0]*26
    countB = [0]*26
    for char in a:
        countA[ord(char)-97] += 1
    for char in b:
        countB[ord(char)-97] += 1
    no = 0
    for i in range(26):
        if countA[i] != countB[i]:
            no = 1
            break
    if no:
        print("NO")
        continue
    yes = 0
    for i in range(26):
        if countA[i] >= 2:
            yes = 1
            break
        if countB[i] >= 2:
            yes = 1
            break
    if yes:
        print("YES")
        continue
    def countRev(s):
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if s[i] > s[j]:
                    count += 1
        return count
    x = countRev(a) - countRev(b)
    if x%2:
        print("NO")
    else:
        print("YES")
