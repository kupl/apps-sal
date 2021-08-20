def over_the_road(address, n):
    return (n - address // 2) * 2 + (not address % 2)
