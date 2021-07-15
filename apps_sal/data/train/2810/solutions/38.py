import string
def solve(arr):
    k = []
    for word in arr:
        count = 0
        for i in range(len(word)):
            if i < 26 and word[i].lower() == string.ascii_lowercase[i]:
                count += 1
        k.append(count)   
    return k

