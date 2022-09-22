from specie import Specie as Specie

#   i.e halogen oxyanions
haloates = lambda halo, min_oxy, max_oxy: {
    Specie((halo, "O"), (1, n_oxygen), charge):
    Specie((f"({halo}O{n_oxygen if n_oxygen > 1 else ''})",), (1,), -1)
    for n_oxygen in range(min_oxy, max_oxy+1) for charge in [0, -1]
}

polyatomics = {
    "chlorates": haloates("Cl", 1, 4),
    "bromates": haloates("Br", 1, 4),
    "iodates":  haloates("I", 1, 4)
}

print(polyatomics["chlorates"].items())