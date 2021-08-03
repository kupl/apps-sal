r = dict(__import__("re").findall(r"(\d{3}).*-\s(.+)",
                                  """
        039 xxx xx xx - Golden Telecom
        050 xxx xx xx - MTS
        063 xxx xx xx - Life:)
        066 xxx xx xx - MTS
        067 xxx xx xx - Kyivstar
        068 xxx xx xx - Beeline
        093 xxx xx xx - Life:)
        095 xxx xx xx - MTS
        096 xxx xx xx - Kyivstar
        097 xxx xx xx - Kyivstar
        098 xxx xx xx - Kyivstar
        099 xxx xx xx - MTS
        """))


def detect_operator(s): return r.get(s[1:4], "no info")
