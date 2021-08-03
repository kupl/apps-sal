def sea_sick(sea):
    return "Throw Up" if (sea.count("~_") + sea.count("_~")) / len(sea) > 0.2 else "No Problem"
