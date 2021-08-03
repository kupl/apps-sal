from typing import Dict, Union


def eval_object(v: Dict[str, Union[str, int]]) -> int:
    """ Make a math operation based on `v` object. """
    return {
        "+": v["a"] + v["b"],
        "-": v["a"] - v["b"],
        "/": v["a"] / v["b"],
        "*": v["a"] * v["b"],
        "%": v["a"] % v["b"],
        "**": v["a"] ** v["b"]
    }.get(v["operation"], 1)
