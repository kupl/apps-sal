def rake_garden(garden):
    return " ".join(i if i in "gravelrock" else "gravel" for i in garden.split())
