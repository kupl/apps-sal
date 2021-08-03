def count_deaf_rats(town):
    return town.replace(" ", "")[0::2].count("O")
