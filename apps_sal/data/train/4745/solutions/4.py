def group_groceries(groceries):
    dict = {"fruit": [], "meat": [], "other": [], "vegetable": []}
    for i in groceries.split(","):
        items = i.split("_")
        if not items[0] in ["fruit", "meat", "vegetable"]:
            dict["other"].append(items[1])
        else:
            dict[items[0]].append(items[1])
    temp = {k: ",".join(sorted(v)) for k, v in dict.items()}
    return "\n".join(f"{i}:{j}" for i, j in temp.items())
