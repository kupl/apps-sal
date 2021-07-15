def sea_sick(sea):
    return "Throw Up" if (sea.count("~_") + sea.count("_~")) > 0.2*len(sea) else "No Problem"
