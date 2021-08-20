def case_unification(str):
    return str.lower() if sum((1 for ch in str if ch.islower())) > len(str) // 2 else str.upper()
