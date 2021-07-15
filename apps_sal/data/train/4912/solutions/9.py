def html_end_tag_by_start_tag(start_tag):
    init = start_tag.split()[0].strip('>').strip('<')
    return f"</{init}>"
