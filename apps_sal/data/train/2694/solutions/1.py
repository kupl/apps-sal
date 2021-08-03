def paul(x):
    val = x.count("kata") * 5 + x.count("Petes kata") * 10 + x.count("eating")
    return 'Super happy!' if val < 40 else 'Happy!' if 40 <= val < 70 else 'Sad!' if 70 <= val < 100 else 'Miserable!'
