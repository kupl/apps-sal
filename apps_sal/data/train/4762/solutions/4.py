def nkotb_vs_homie(requirements):
    return [f"{v.split()[2].title()}! Homie dont play that!" for lst in requirements for v in lst] + [", ".join(f"{['','and '][a=='microservices']}{len(b)} {a}" for a, b in zip(["monitoring objections", "automation", "deployment pipeline", "cloud", "microservices"], requirements)) + "."]
