def group_groceries(groceries):
    categories = {"fruit": [], "meat": [], "other": [], "vegetable": []}
    for entry in groceries.split(","):
        category, item = entry.split("_")
        categories[category if category in categories else "other"].append(item)
    return "\n".join([f"{category}:{','.join(sorted(items))}" for category, items in categories.items()])
