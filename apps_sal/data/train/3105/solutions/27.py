def count_sheep(n):
    count = 0
    details = []
    for i in range(1, n + 1):
        count += 1
        details.append(str(count) + " sheep...")

    return "".join(details)
