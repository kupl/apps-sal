def multi_table(table):
    results = ""
    for i in range(1,10):
        results += f"{i} * {table} = {i * table}\n"
    return results + f"{10} * {table} = {10 * table}"

