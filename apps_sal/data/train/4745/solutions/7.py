def group_groceries(groceries):
    res = {"fruit": [], "meat": [], "other": [], "vegetable": []}
    for item in groceries.split(','):
        category, name = item.split('_')
        res.get(category, res["other"]).append(name)
    return '\n'.join(f"{k}:{','.join(sorted(v))}" for k, v in res.items())
