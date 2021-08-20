n = int(input())
a = list(map(int, input().split()))
q = []
temp = 0
depth = 0
bracket = [0, 0]
brac_count = [0, 0]
brac_ind = [0, 0]
for (i, v) in enumerate(a):
    if v == 1 or v == 3:
        if v == 1:
            if brac_count[0] == 0:
                brac_ind[0] = i
            brac_count[0] += 1
        else:
            if brac_count[1] == 0:
                brac_ind[1] = i
            brac_count[1] += 1
        if not q or v != q[-1]:
            temp += 1
        q.append(v)
    else:
        depth = max(temp, depth)
        if len(q) < 2 or q[-1] != q[-2]:
            temp -= 1
        q.pop()
        if v == 2:
            brac_count[0] -= 1
            if brac_count[0] == 0:
                bracket[0] = max(bracket[0], i - brac_ind[0] + 1)
        else:
            brac_count[1] -= 1
            if brac_count[1] == 0:
                bracket[1] = max(bracket[1], i - brac_ind[1] + 1)
print(depth, bracket[0], bracket[1])
