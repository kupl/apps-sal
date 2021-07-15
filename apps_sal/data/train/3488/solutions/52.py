def eval_object(v):
    return {
        "+": v["a"] + v["b"],
        "-": v["a"] - v["b"],
        "/": v["a"] / v["b"],
        "*": v["a"] * v["b"],
        "%": v["a"] % v["b"],
        "**": v["a"] ** v["b"]
    }[v.get("operation", 1)]

