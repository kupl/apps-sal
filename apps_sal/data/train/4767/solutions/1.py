from operator import gt, lt


def longest_comb(arr, command):
    (max_length, stack, op) = (1, [], {'>': gt, '<': lt}[command[0]])
    for n in arr[::-1]:
        for i in range(len(stack)):
            if op(n, stack[i][0]):
                stack.append([n] + stack[i])
                max_length = max(max_length, len(stack[-1]))
        stack.append([n])
    ret = [seq for seq in stack if len(seq) == max_length][::-1]
    return [] if max_length < 3 else ret if len(ret) > 1 else ret.pop()
