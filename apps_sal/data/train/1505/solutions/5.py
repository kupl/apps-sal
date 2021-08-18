def is_seq_brackets_right(input_seq):
    stack = []
    highest_depth = 0
    highest_depth_index = 0
    max_inner_symbols_no = 0
    max_inner_symbols_index = 0
    for index_ in range(len(input_seq)):
        i = input_seq[index_]
        if i == "1":
            stack.append(["1", index_])
        else:
            temp = stack.pop(-1)
            if index_ - temp[1] + 1 > max_inner_symbols_no:
                max_inner_symbols_no = index_ - temp[1] + 1
                max_inner_symbols_index = temp[1]

        if len(stack) > highest_depth:
            highest_depth = len(stack)
            highest_depth_index = index_
    return len(stack) == 0, highest_depth, highest_depth_index + 1, max_inner_symbols_no, max_inner_symbols_index + 1


N = int(input().strip())
input_string = input().strip()
bracket_input = input_string.replace(" ", "")
ans = is_seq_brackets_right(bracket_input)
print(ans[1], " ", ans[2], " ", ans[3], " ", ans[4])
