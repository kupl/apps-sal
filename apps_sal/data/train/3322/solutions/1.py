translation = str.maketrans("IREASGTBOlzeasbtgo", "123456780123456790")


def cypher(s):
    return s.translate(translation)
