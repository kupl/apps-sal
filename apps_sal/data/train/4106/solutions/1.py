def self_converge(n, seen=None):
    s, seen = "".join(sorted(str(n))), set() if seen is None else seen
    s = f"{int(s[::-1]) - int(s):0{len(s)}d}"
    return len(seen) + 1 if int(s) and s in seen else self_converge(s, seen | {s}) if int(s) else -1

