geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    ans = birds.copy()
    for i in birds:
        if i in geese:
            ans.remove(i)
    return ans
