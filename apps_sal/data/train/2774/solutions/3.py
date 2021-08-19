def is_balanced(source, caps):
    (oldLen, source) = (len(source), ''.join((l for l in source if l in caps)))
    while oldLen != len(source):
        oldLen = len(source)
        for i in range(0, len(caps), 2):
            source = source.replace(caps[i:i + 2], '')
    return len(source) == 0
