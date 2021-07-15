def sort_string(stg, ordering):
    return "".join(sorted(stg, key=lambda c: ordering.index(c) if c in ordering else float("inf")))
