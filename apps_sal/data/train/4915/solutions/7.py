def rake_garden(garden):
    garden = garden.split(" ")
    for i in range(len(garden)):
        if garden[i] != "gravel" and garden[i]!= "rock":
            garden[i] = "gravel"
    return " ".join(garden)
