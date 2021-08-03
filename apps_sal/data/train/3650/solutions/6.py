def solve(arr):
    stack = []
    for num in arr:
        branches = arr.copy()
        branches.remove(num)
        stack = [([num], branches)]
        while len(stack) != 0:
            (current, remaining) = stack.pop()
            if len(remaining) == 0:
                return current
            x = current[len(current) - 1]
            valid_leaves = [leaf for leaf in remaining if x / 3 == leaf or x * 2 == leaf]
            for valid in valid_leaves:
                valid_current = current.copy()
                valid_current.append(valid)
                valid_remaining = remaining.copy()
                valid_remaining.remove(valid)
                stack.append((valid_current, valid_remaining))
