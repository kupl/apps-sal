def reverse_alternate(stg):
    return " ".join(word[::-1] if i & 1 else word for i, word in enumerate(stg.split()))
