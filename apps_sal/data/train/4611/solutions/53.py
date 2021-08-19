def animals(heads, legs):
    (ch, co) = (heads * 2 - legs / 2, legs / 2 - heads)
    if ch < 0 or co < 0 or (not ch.is_integer()) or (not co.is_integer()):
        return 'No solutions'
    else:
        return (ch, co)
