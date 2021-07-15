def cycle(sequence):
    collector = []
    for s in sequence:
        if s in collector:
            mu = collector.index(s)
            return [mu, len(collector) - mu]
        collector.append(s)
    return []
