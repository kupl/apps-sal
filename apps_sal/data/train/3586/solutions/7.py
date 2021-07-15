def html(t, *args, **kwargs):
    s = "".join(f' {"class" if x == "cls" else x}="{kwargs[x]}"' for x in kwargs)
    return f"<{t}{s} />" if not args else "\n".join(f"<{t}{s}>{x}</{t}>" for x in args)
