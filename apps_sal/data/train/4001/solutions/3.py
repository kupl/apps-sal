def dot(w, h):
    sep, row = "+---" * w + "+\n", "| o " * w + "|\n"
    return (sep + row) * h + sep.strip()
