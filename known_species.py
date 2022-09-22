from specie import Specie as Specie

#   i.e halogen oxyanions
oxyanions = lambda halo, min_oxy, max_oxy: {
    Specie((halo, "O"), (1, n_oxygen), charge):
    Specie((f"({halo}O{n_oxygen if n_oxygen > 1 else ''})",), (1,), -1)
    for n_oxygen in range(min_oxy, max_oxy+1) for charge in [0, -1]
}

polyatomics = {
    "chlorates": oxyanions("Cl", 1, 4),
    "bromates": oxyanions("Br", 1, 4),
    "iodates":  oxyanions("I", 1, 4)
}

print(polyatomics["chlorates"].items())