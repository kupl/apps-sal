def triple_trouble(one, two, three):
    result_str = ''
    for (o, tw, th) in zip(one, two, three):
        result_str += o + tw + th
    return result_str
