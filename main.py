from collections import namedtuple

from specie import interpret

f = namedtuple("Yes", "x")

print(interpret(input()))
print(f(3))