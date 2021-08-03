def vowel_2_index(s):
    return "".join(str(i + 1) if s[i].lower() in "aeuoi" else s[i] for i in range(len(s)))
