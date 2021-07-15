def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')
