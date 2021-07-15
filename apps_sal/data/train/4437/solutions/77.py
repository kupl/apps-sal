def cookie(x):
    switcher = {
        str: "Zach!",
        float: "Monica!",
        int: "Monica!",
        bool: "the dog!"
    }
    return "Who ate the last cookie? It was " + switcher.get(type(x))

