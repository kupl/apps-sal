def html(tag, *contents, **attr):
    openTag = tag + ''.join(f' {"class" if k=="cls" else k}="{v}"' for k, v in attr.items())

    return '\n'.join(f'<{openTag}>{c}</{tag}>' for c in contents) or f'<{openTag} />'
