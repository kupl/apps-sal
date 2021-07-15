def over_the_road(address, n):
    return (n - address // 2) * 2 if address % 2 else (n - address // 2) * 2 + 1
