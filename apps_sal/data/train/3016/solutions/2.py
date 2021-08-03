notes = ["C", ["C#", "Db"], "D", ["D#", "Eb"], "E", "F", ["F#", "Gb"], "G", ["G#", "Ab"], "A", ["A#", "Bb"], "B"]
mom = {(3, 4): "Minor", (4, 3): "Major"}
levels = {
    x: i
    for i, xs in enumerate(notes)
    for x in ([xs] if isinstance(xs, str) else xs)
}


def minor_or_major(chord):
    xs = [levels.get(c) for c in chord.split()]
    if None in xs:
        return "Not a chord"
    deltas = tuple((b - a) % len(notes) for a, b in zip(xs, xs[1:]))
    return mom.get(deltas, "Not a chord")
