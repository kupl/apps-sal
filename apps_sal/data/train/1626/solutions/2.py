def getGreatest(n, d, prefix):
    rows = 9 * 10 ** (d - 1)
    triangle = rows * (d + rows * d) // 2
    l = 0
    r = triangle
    while l < r:
        mid = l + (r - l >> 1)
        triangle = mid * prefix + mid * (d + mid * d) // 2
        prevTriangle = (mid - 1) * prefix + (mid - 1) * (d + (mid - 1) * d) // 2
        nextTriangle = (mid + 1) * prefix + (mid + 1) * (d + (mid + 1) * d) // 2
        if triangle >= n:
            if prevTriangle < n:
                return prevTriangle
            else:
                r = mid - 1
        elif nextTriangle >= n:
            return triangle
        else:
            l = mid
    return l * prefix + l * (d + l * d) // 2


ns = [1, 2, 3, 100, 2100, 31000, 999999999999999999, 1000000000000000000, 999999999999999993]


def solve(n):
    debug = 1
    d = 0
    p = 0.1
    prefixes = [0]
    sections = [0]
    while sections[d] < n:
        d += 1
        p *= 10
        rows = int(9 * p)
        triangle = rows * (d + rows * d) // 2
        section = rows * prefixes[d - 1] + triangle
        sections.append(sections[d - 1] + section)
        prefixes.append(prefixes[d - 1] + rows * d)
    section = sections[d - 1]
    n = n - section
    rows = getGreatest(n, d, prefixes[d - 1])
    n = n - rows
    d = 1
    while prefixes[d] < n:
        d += 1
    if prefixes[d] == n:
        return 9
    prefix = prefixes[d - 1]
    n -= prefix
    countDDigitNums = n // d
    remainder = n % d
    prev = 10 ** (d - 1) - 1
    num = prev + countDDigitNums
    if remainder:
        return int(str(num + 1)[remainder - 1])
    else:
        s = str(num)
        return int(s[len(s) - 1])
