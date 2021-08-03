def eval_object(v):
    return eval(str(v.get("a")) + v.get("operation") + str(v.get("b")))
