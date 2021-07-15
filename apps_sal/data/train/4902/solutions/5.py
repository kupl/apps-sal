def show_me(instname):
    hi = f"Hi, I'm one of those {instname.__class__.__name__}s!"
    fields = sorted(vars(instname))
    if len(fields) == 1:
        return f"{hi} Have a look at my {fields[0]}."
    else:
        return f"{hi} Have a look at my {', '.join(fields[:-1])} and {fields[-1]}."
