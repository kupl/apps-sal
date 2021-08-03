def unlucky_days(y):
    count = 0  # Clean & Pure Math Example
    for m in range(3, 15):
        if m == 13:
            y -= 1
        if (y % 100 + (y % 100 // 4) + (y // 100) // 4 - 2 * (y // 100) + 26 * (m + 1) // 10 + 12) % 7 == 5:
            count += 1
    return count
