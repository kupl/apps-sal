def memorysize_conversion(memorysize):
    [value, unit] = memorysize.split(" ")
    kibis = ["KiB", "MiB", "GiB", "TiB"]
    kilos = ["kB", "MB", "GB", "TB"]
    if unit in kibis:
        return (str(round(float(value) * pow(1.024, kibis.index(unit) + 1), 3)) + " " + kilos[kibis.index(unit)])
    else:
        return (str(round(float(value) / pow(1.024, kilos.index(unit) + 1), 3)) + " " + kibis[kilos.index(unit)])
