def longest(s1, s2):
    results = []
    for records in s1:
        if records not in results:
            results.append(records)
    for records in s2:
        if records not in results:
            results.append(records)
    results = sorted(results)
    return "".join(results)

