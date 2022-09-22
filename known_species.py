from specie import Specie as Specie


#   i.e halogen oxyanions
def oxyanions(victim, oxy_values, r_charge, num_victim=1, charge_increment=0):
    #   When you expand an oneliner to an entire paragraph to flex and readability
    return {
        Specie((victim, "O"), (num_victim, n_oxygen), charge) if n_oxygen != -1
        else Specie((victim,), (num_victim,), charge):
            Specie((f"({victim}{num_victim if num_victim > 1 else ''}" +
                    f"{'O' + str(n_oxygen) if n_oxygen > 1 else 'O' if n_oxygen == 1 else ''})",),
                   (1,), r_charge + charge_increment * i)
        for i, n_oxygen in enumerate(oxy_values) for charge in [0, r_charge + charge_increment * i]
    }


polyatomics = {
    #   Halogen oxyanions
    "chlorates": oxyanions("Cl", range(1, 5), -1),
    "bromates": oxyanions("Br", range(1, 5), -1),
    "iodates": oxyanions("I", range(1, 5), -1),
    #   Boron oxyanions
    "borates": {**oxyanions("B", range(2, 4), -1, charge_increment=-2), **oxyanions("B", [7], -2, num_victim=4)},
    #   Carbon family oxyanions
    "carbonates": oxyanions("C", range(3, 4), -2),
    "silicates": {**oxyanions("Si", range(3, 5), -2, charge_increment=-2), **oxyanions("Si", [7], -6, num_victim=2)},
    #   Nitrogen family oxyanions
    "nitrates": oxyanions("N", range(2, 4), -1),
    "phosphates": oxyanions("P", range(4, 5), -3),
    #   Also doesn't include the special sulfates formed in sulfuric acid
    "peroxides": oxyanions("O", [-1], -2, num_victim=2),
    "sulfates": {**oxyanions("S", range(3, 5), -2), **oxyanions("S", range(3, 4), -2, num_victim=2)},
    #   To add cyanates we need to be able to add a whole group, i.e 'CN' as itself
    "cyanates": oxyanions("CN", [-1, 1], -1)
}
