def namelist(names):

    names = [hash["name"] for hash in names]
    output = names[:-2]
    output.append(" & ".join(names[-2:]))
    return ", ".join(output)
