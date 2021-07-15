def namelist(names):
    return ", ".join(person["name"] for person in (names if len(names)<2 else names[:-1])) + (" & " + names[-1]["name"] if len(names)>1 else "")
