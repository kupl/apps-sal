def actually_really_good(foods):
    def formatter(pairFood):
        return (f(s) for f, s in zip((str.capitalize, str.lower), pairFood))
    START = "You know what's actually really good? "
    return START + ("Nothing!" if not foods else
                    "{1} and {0}{2}.".format("more " * (len(foods) == 1), *formatter(foods * 2 if len(foods) == 1 else foods[:2])))
