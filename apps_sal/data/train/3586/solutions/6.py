def html(tag, *contents, **attrs):
    attr_ls = [f'{"class" if k=="cls" else k}="{v}"' for k, v in attrs.items()]
    if not contents:
        return f"<{' '.join((tag, *attr_ls))} />"
    else:
        return '\n'.join(f"<{' '.join((tag, *attr_ls))}>{content}</{tag}>" for content in contents)
