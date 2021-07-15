def is_kiss(s):
    s = s.split()
    n = len(s)
    return "Good work Joe!" if all(len(x) <= n for x in s) else "Keep It Simple Stupid"
