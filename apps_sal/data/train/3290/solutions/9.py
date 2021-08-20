def get_ages(s, d):
    return (lambda *a: None if any((x < 0 for x in (*a, s, d))) else a)((s + d) / 2, (s - d) / 2)
