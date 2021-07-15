def word_problem(rules: List[Tuple[str, str]], from_str: str, to_str: str, applications: int) -> bool:
    rec = lambda s,n: s == to_str or n and any(s[i:].startswith(x) and rec(s[:i] + y + s[i+len(x):], n-1) for i in range(len(s)) for x,y in rules)
    return rec(from_str, applications)
