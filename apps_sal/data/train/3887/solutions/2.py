def pattern(n):
    if n == 1:
        return "1"
    if n < 1:
        return ""
    top = "\n".join([" " * (n - 1) + str(i % 10) * n + " " * (n - 1) for i in range(1, n)])
    result = [top]
    nums = [str(i % 10) for i in range(1, n)]
    result.append("\n".join(["".join(nums) + str(n % 10) * n + "".join(nums[::-1])] * n))
    result.append(top[::-1])
    return "\n".join(result)
