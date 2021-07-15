from re import search
def html_end_tag_by_start_tag(tag):
    return f"</{search('<[a-z]+',tag).group()[1:]}>"
