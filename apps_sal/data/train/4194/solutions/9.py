def next_version(version):
    c, s = version.count(".") + 1, version.replace(".", "")
    n = f"{int(s)+1:0{len(s)}d}"[::-1]
    return (".".join(n[i] for i in range(c)) + n[c:])[::-1]
