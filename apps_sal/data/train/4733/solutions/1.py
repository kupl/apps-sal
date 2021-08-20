def rot_energies(rot, energy_min, energy_max):
    if rot <= 0:
        return []
    else:
        return [rot * energy * (energy + 1) for energy in range(energy_min, energy_max + 1)]
