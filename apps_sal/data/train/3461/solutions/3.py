def common_ground(s1, s2):
    s1, s2 = set(s1.split()), s2.split()
    return " ".join(sorted((word for word in set(s2) if word in s1), key=s2.index)) or "death"
