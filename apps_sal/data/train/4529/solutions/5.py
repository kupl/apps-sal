def truncate_string(s, n): return s[:n - 3 * (3 < n < len(s))] + '...' * (n < len(s))
