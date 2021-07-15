def top3(*args):
    return [item[0] for item in sorted(zip(*args), key=lambda x: x[1]*x[2], reverse=True)[:3]]
