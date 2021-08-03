# cook your dish here

def is_seq_brackets_right(input_seq):
    stack = []
    highest_depth = 0
    highest_depth_index = 0
    max_inner_symbols = []
    max_inner_symbols_no = 0
    max_inner_symbols_index = 0
    for index_ in range(len(input_seq)):
        i = input_seq[index_]
        if i == "(":
            stack.append("(")
            max_inner_symbols.append([index_, 1, True])
        else:
            stack.pop(-1)
            max_inner_symbols.pop(-1)

        for j in range(len(max_inner_symbols)):
            max_inner_symbols[j][1] = max_inner_symbols[j][1] + 1
            if max_inner_symbols[j][1] > max_inner_symbols_no:
                max_inner_symbols_no = max_inner_symbols[j][1]
                max_inner_symbols_index = max_inner_symbols[j][0]

        if len(stack) > highest_depth:
            highest_depth = len(stack)
            highest_depth_index = index_
    return len(stack) == 0, highest_depth, highest_depth_index + 1, max_inner_symbols_no, max_inner_symbols_index + 1


N = int(input().strip())
input_string = input().strip()
bracket_input = input_string.replace(" ", "").replace("1", "(").replace("2", ")")
ans = is_seq_brackets_right(bracket_input)
print(ans[1], " ", ans[2], " ", ans[3], " ", ans[4])
