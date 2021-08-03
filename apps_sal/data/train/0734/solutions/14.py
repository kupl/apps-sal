# cook your dish here
# print("Odd")
from collections import Counter

for _ in range(int(input())):

    n = int(input())
    li = [int(x) for x in input().split()]
    # n = 2
    # li  = [1,1]

    inp_ord = list(enumerate(li))
    cow = Counter(li)
    max_freq = cow.most_common(1)[0][1]

    if max_freq > n - max_freq:
        print("No")

    else:
        sorted_input = sorted(inp_ord, key=lambda x: x[1])

        foo = n - max_freq
        for i in range(foo):

            current_element = sorted_input[i][1]
            curr_pos = sorted_input[i][0]

            toSwapIndex = i + max_freq

            swap_partner = sorted_input[toSwapIndex][1]
            swap_position = sorted_input[toSwapIndex][0]

            sorted_input[i] = curr_pos, swap_partner
            sorted_input[toSwapIndex] = swap_position, current_element

        op_list = sorted(sorted_input, key=lambda x: x[0])
        bar = [y for x, y in op_list]
        print("Yes")
        print(*bar)
