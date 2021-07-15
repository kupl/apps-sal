def args_to_string(args):
    for i in args:
        if len(i) > 1 and type(i) != str:
            i[0] = f"--{i[0]}" if len(i[0]) > 1 else f"-{i[0]}"
    return " ".join(i if type(i) != list else " ".join(i) for i in args)
