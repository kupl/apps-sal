def square_sums_row(n):
    stack = [(set(range(1, n + 1)), [])]
    while stack:
        (existing_nums, out) = stack.pop()
        if len(out) == n:
            return out
        for num in existing_nums:
            if not out or not (num + out[-1]) ** 0.5 % 1:
                stack.append((existing_nums - {num}, out + [num]))
    return False
