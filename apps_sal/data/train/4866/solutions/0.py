def split_all_even_numbers(numbers, split_type):
    result = []
    for a in numbers:
        if a % 2:
            result.append(a)
        else:
            pairs = [(b, a - b) for b in range(1, a // 2 + 1, 2) if a - b % 2]
            if split_type == 0:
                result.extend(pairs[-1])
            elif split_type == 1:
                result.extend(pairs[0])
            elif split_type == 2:
                for c, _ in reversed(pairs):
                    quo, rem = divmod(a, c)
                    if not rem:
                        result.extend([c] * quo)
                        break
            elif split_type == 3:
                result.extend([1] * a)
    return result

