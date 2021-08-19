def is_john_lying(a, b, s):
    dest_dist = abs(a) + abs(b)
    return dest_dist == s or (dest_dist < s and (not (dest_dist - s) % 2))
