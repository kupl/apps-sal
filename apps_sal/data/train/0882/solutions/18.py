test = int(input())
for _ in range(test):
    string1 = input().strip()
    string2 = input().strip()
    hashMap1 = {}
    hashMap2 = {}
    for i in string1:
        if i in hashMap1:
            hashMap1[i] += 1
        else:
            hashMap1[i] = 1

    for i in string2:
        if i in hashMap2:
            hashMap2[i] += 1
        else:
            hashMap2[i] = 1

    total = 0
    for i in hashMap2:
        if i in hashMap1:
            total = total + min(hashMap1[i], hashMap2[i])
    print(total)
