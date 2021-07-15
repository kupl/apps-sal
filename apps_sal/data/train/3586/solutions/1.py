def html(tag, *args, **kwargs):
    open = tag + ''.join(f' {"class" if k == "cls" else k}="{v}"' for k,v in kwargs.items())
    return '\n'.join(f"<{open}>{a}</{tag}>" for a in args) or f"<{open} />"
