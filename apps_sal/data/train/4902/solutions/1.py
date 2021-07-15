def show_me(instname):
    classname = instname.__class__.__name__
    attrs = " and".join(", ".join(attr for attr in sorted(instname.__dict__.keys())).rsplit(",", 1))
    return f"Hi, I'm one of those {classname}s! Have a look at my {attrs}."
