# cook your dish here

T = int(input())
l = list(map(int, input().strip().split(" ")))

depth = 0
max_depth = 0
max_depth_index = 0

max_l=0
max_l_index=0
last_zero=-1

for i in range(T):
    if l[i] == 1:
        depth += 1
        if depth > max_depth:
            max_depth = depth
            max_depth_index = i + 1
    else:
        depth-=1
        if depth == 0:
            length = i - last_zero
            if length > max_l:
                max_l = length
                max_l_index = last_zero + 2
            last_zero = i
        
print(max_depth, max_depth_index, max_l, max_l_index)

"""
2 4 6 9
"""
