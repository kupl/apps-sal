def html_end_tag_by_start_tag(start_tag):
    if " " in start_tag:
        a = start_tag.split(" ")
        return "</" + a[0][1:] + ">"
    else:
        return "</" + start_tag[1:-1] + ">"
