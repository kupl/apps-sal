def target_game(values):
    dicto = {}

    def target_games(values, ind=0, reloaded=True, sumo=0):
        key = f"ind {ind} sumo {sumo} reloaded {reloaded}"
        if key in dicto:
            return dicto[key]
        if ind >= len(values):
            return sumo
        while values[ind] < 0:
            ind += 1
            reloaded = True
            if ind == len(values):
                return sumo
        if reloaded:
            d = target_games(values, ind + 1, not reloaded, sumo + values[ind])
        elif not reloaded:
            d = target_games(values, ind + 1, not reloaded, sumo)
        f = target_games(values, ind + 1, reloaded, sumo)
        dicto[key] = max(d, f)
        return dicto[key]
    return target_games(values)
