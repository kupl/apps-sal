def convert_recipe(recipe):
    import math
    out=[]
    for x in recipe.split(" "):
        if x in ["tbsp", "tsp"]:
            calc = math.ceil(eval("{}*{}".format(out[-1], "15" if x == "tbsp" else "5")))
            out.append(x)
            out.append("({}g)".format(calc))
        else:
            out.append(x)
    return " ".join(out)
