def area_or_perimeter(l, w):
    ans = 2 * l + 2 * w
    if l == w:
        ans = l * w
    return ans
