def generate_hashtag(s):
    return "#{}".format("".join(s.title().strip().split())) if len("#{}".format("".join(s.title().strip().split())))<=140 and s.strip() != "" else False
