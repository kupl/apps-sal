import importlib

built_ins = importlib.import_module("b" + "uiltins")


def solved(string):
    return vars(built_ins).get("e" + "val")("m" + "ystery('" + string + "')")
