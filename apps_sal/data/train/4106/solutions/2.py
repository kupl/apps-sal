def self_converge(n):
    s, seen = str(n), set()
    while not s in seen:
        seen.add(s)
        s = "".join(sorted(s))
        s = f"{int(s[::-1]) - int(s):0{len(s)}d}"
    return len(seen) if int(s) else -1

