def count_sheep(n):
    if n == 0:
        return ""
    else:
        count = "1 sheep..."
        for i in range(2, n + 1):
            count += f"{i} sheep..."

    return count
