def html(tag_name, *args, **kwargs):
    attributes = []
    for key, value in kwargs.items():
        if key == "cls":
            key = "class"
        attributes.append(f'{key}="{value}"')
    
    if len(args) == 0:
        return f"<{tag_name}{'' if len(attributes) == 0 else ' ' + ' '.join(attributes)} />"
    
    closing_tags = []
    for arg in args:
        closing_tags.append(f"<{tag_name}{'' if len(attributes) == 0 else ' ' + ' '.join(attributes)}>{arg}</{tag_name}>")
    return "\n".join(closing_tags)
