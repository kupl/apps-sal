input()
brackets = list(map(int, input().split()))
depth = 0
rn_longest = 0
sq_longest = 0
alt_depth = 0
max_alt_depth = 0
last_alt = (alt_depth, 1 if brackets[0] == 3 else 3)
same_rep = [0]
sq_start = (-2, 0) # index, -2 if not found
rn_start = (-2, 0) # , depth - 1

for i in range(len(brackets)):
    b = brackets[i]
    if b in [1, 3]:
        depth += 1
        if b != last_alt[1]:
            alt_depth += 1
            last_alt = (alt_depth, b)
            max_alt_depth = max(alt_depth, max_alt_depth)
            same_rep += [0]
        else:
            same_rep[-1] += 1
        if sq_start[0] == -2 and b == 3:
            sq_start = (i - 1, depth - 1)
        elif rn_start[0] == -2 and b == 1:
            rn_start = (i - 1, depth - 1)
    else:
        depth -= 1
        if b == last_alt[1] + 1:
            if same_rep[-1] > 0:
                same_rep[-1] -= 1
            else:
                alt_depth -= 1
                last_alt = (alt_depth, 1 if b == 4 else 3)
                same_rep.pop(-1)
        if sq_start[1] == depth and b == 4:
            sq_longest = max(sq_longest, i - sq_start[0])
            sq_start = (-2, 0)
        elif rn_start[1] == depth and b == 2:
            rn_longest = max(rn_longest, i - rn_start[0])
            rn_start = (-2, 0)
    # print(i + 1, alt_depth, same_rep)
    if depth == 0:
        if i < len(brackets) - 1:
            last_alt = (alt_depth, 1 if brackets[i+1] == 3 else 3)
print(max_alt_depth, rn_longest, sq_longest)
