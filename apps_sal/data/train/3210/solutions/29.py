get_strings = lambda city: "".join(list(dict.fromkeys(["{}:{},".format(i, "*" * city.lower().count(i)) for i in city.lower() if i != " "]))).rstrip(",")
