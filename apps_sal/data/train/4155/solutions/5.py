def solve(a, b):
    s = {'0', '1', '6', '8', '9'}
    total = 0
    for i in range(a, b):
        if i < 10:
            if i in (0, 1, 8):
                total += 1
        else:
            n = str(i)
            if set(n).issubset(s):
                left, right = 0, len(n) - 1
                while left <= right:
                    ln = n[left]
                    rn = n[right]
                    if left == right and ln in '69':
                        break
                    if ln + rn in ('69', '96') or (ln == rn and ln in '018'):
                        left += 1
                        right -= 1
                    else:
                        break
                if left > right:
                    total += 1

            else:
                continue
    return total
