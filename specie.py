"""
Contains the functions used to interpret strings into a list with their data, do corrections to data, and obtain data
on a specie or its specific data.
"""
from collections import namedtuple

#   Species should be of the form AaBb(Cc)[D-]
Specie = namedtuple("Specie", "composing_groups subscripts charge")


def interpret(specie: str):
    def is_group(char: str) -> bool:
        return char.isalpha() or char == "(" or char == ")"

    def is_subscript(char: str) -> bool:
        return char.isnumeric()

    def find_group(ind: int) -> (str, int):
        #   Returns subscript, end index
        group: str = ""

        i: int = 0
        while ind < len(specie) and i < 2:
            char = specie[ind]

            if char == "(":
                start_index = ind
                while specie[ind] != ")":
                    ind += 1

                return specie[start_index:ind+1], ind+1

            if char.isupper():
                group += char
                ind += 1
                break

            if not is_group(char):
                break

            group += char
            ind += 1
            i += 1

        while ind < len(specie):
            char = specie[ind]

            if not (char.isalpha()) or char.isupper():
                break

            group += char
            ind += 1

        return group, ind

    def find_subscript(ind: int) -> (int, int):
        #   Returns subscript, end index
        #   Easier and better implementation uses str and just converts to int at the end
        subscript: str = ""
        while ind < len(specie):
            char: str = specie[ind]

            if not is_subscript(char) and not char.islower():
                break

            subscript += char
            ind += 1

        if subscript != "":
            return int(subscript), ind

        return 0, ind

    def find_charge(start_index: int) -> int:
        if not (start_index < len(specie)):
            return 0

        pot_charge: str = specie[start_index:-1].strip("[").strip("]")
        try:
            charge = int(pot_charge)
            return charge
        except ValueError:
            return 0

    index: int = 0
    groups: list[str] = []
    subscripts: list[int] = []
    while index <= len(specie):
        group, index = find_group(index)
        subscript, index = find_subscript(index)

        if group == "":
            charge = find_charge(index)
            decomposed_specie = Specie(composing_groups=groups, subscripts=subscripts, charge=charge)

            return decomposed_specie

        groups.append(group)
        subscripts.append(subscript)
