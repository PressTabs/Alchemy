from specie import Specie as Specie


#   i.e halogen oxyanions
def oxyanions(victim, oxy_values, r_charge):
    return {
        Specie((victim, "O"), (1, n_oxygen), charge):
            Specie((f"({victim}O{n_oxygen if n_oxygen > 1 else ''})",), (1,), -1)
        for n_oxygen in oxy_values for charge in [0, r_charge]
    }


polyatomics = {
    #   Halogen oxyanions
    "chlorates": oxyanions("Cl", range(1, 5), -1),
    "bromates": oxyanions("Br", range(1, 5), -1),
    "iodates": oxyanions("I", range(1, 5), -1),
    #   Boron oxyanions, not including tetraborate or borite (cus I need to write better functions)
    "borates": oxyanions("B", range(3, 4), -3),
    #   Carbon family oxyanions, doesn't include all the (wonderful) terrible silicates
    "carbonates": oxyanions("C", range(3, 4), -2),
    "silicates": oxyanions("Si", range(3, 4), -2),
    #   Nitrogen family oxyanions
    "nitrates": oxyanions("N", range(2, 4), -1),
    "phosphates": oxyanions("P", range(4, 5), -3),
    #   Oxygen family oxyanions (not including the peroxides, ozone, or thiosulfate)
    #   Also doesn't include the special sulfates formed in sulfuric acid
    "sulfates": oxyanions("S", range(3, 5), -2)
}
