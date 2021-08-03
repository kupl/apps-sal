def common_ground(s1, s2):
    return " ".join(sorted(set(s1.split(" ")).intersection(s2.split(" ")), key=s2.split(" ").index)) or "death"
