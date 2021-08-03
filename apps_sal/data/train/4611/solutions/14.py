def animals(heads, legs):
    return (2 * heads - legs // 2, legs // 2 - heads) if not legs % 2 and 2 * heads >= legs // 2 >= heads >= 0 else "No solutions"
