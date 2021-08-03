def mutate_my_strings(s1, s2):
    if s1 == s2:
        return f"{s1}\n"
    return f"{s1}\n" + "\n".join(f"{s2[:i+1]}{s1[i+1:]}" for i in range(len(s1)) if s1[i] != s2[i]) + "\n"
