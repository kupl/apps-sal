def encode(s):
    return ''.join(({'G': 'A', 'A': 'G', 'g': 'a', 'a': 'g', 'D': 'E', 'E': 'D', 'd': 'e', 'e': 'd', 'R': 'Y', 'Y': 'R', 'r': 'y', 'y': 'r', 'P': 'O', 'O': 'P', 'p': 'o', 'o': 'p', 'L': 'U', 'U': 'L', 'l': 'u', 'u': 'l', 'K': 'I', 'I': 'K', 'k': 'i', 'i': 'k'})[c] if c in {'G': 'A', 'A': 'G', 'g': 'a', 'a': 'g', 'D': 'E', 'E': 'D', 'd': 'e', 'e': 'd', 'R': 'Y', 'Y': 'R', 'r': 'y', 'y': 'r', 'P': 'O', 'O': 'P', 'p': 'o', 'o': 'p', 'L': 'U', 'U': 'L', 'l': 'u', 'u': 'l', 'K': 'I', 'I': 'K', 'k': 'i', 'i': 'k'} else c for c in s)
decode = encode
