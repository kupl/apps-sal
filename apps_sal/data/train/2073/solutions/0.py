def maximum_xor_secondary(sequence):
    stack, answer = [], 0
    for x in sequence:
        while stack:
            answer = max(answer, stack[-1] ^ x)
            if stack[-1] > x:
                break
            else:
                stack.pop()
        stack.append(x)

    return answer


size, num = input(), [int(x) for x in input().split()]


print(maximum_xor_secondary(num))
