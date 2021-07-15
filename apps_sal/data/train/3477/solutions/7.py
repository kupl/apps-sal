def sort_string(s, ordering):
    result = sorted([c for c in s if c in ordering], key=ordering.find)
    result.extend([c for c in s if c not in ordering])
    return ''.join(result)
