def most_common(stg):
    return "".join(sorted(stg, key=stg.count, reverse=True))
