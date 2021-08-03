def replace_exclamation(s):
    return ''.join("!" if let.lower() in ['a', 'e', 'i', 'o', 'u'] else let for let in s)
