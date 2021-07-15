def replace_exclamation(s):
    return "".join("!" if s[n] in "aeiouAEIOU" else s[n] for n in range(len(s)))
