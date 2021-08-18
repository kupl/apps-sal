import sys
n = int(input().strip())
stringa = input().strip().split()
stringa = ''.join(stringa)
counter = 0
max_width = 0
max_depth = 0
for i in range(n):
    if stringa[i] == '1':
        if counter == 0:
            start = i
        counter += 1
    else:
        if counter > max_depth:
            max_depth = counter
            depth_idx = i
        counter -= 1
        if counter == 0:
            end = i
            if end - start + 1 > max_width:
                max_width = end - start + 1
                start_idx = start + 1
print(max_depth, depth_idx, max_width, start_idx)
