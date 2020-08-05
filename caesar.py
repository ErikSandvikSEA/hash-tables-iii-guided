# caesar ciper
# hash table as a map between data values
# GOATS => JEHFN
encode_table = {
    "A": "H",
    "B": "Z",
    "C": "Y",
    "D": "W",
    "E": "O",
    "F": "R",
    "G": "J",
    "H": "D",
    "I": "P",
    "J": "T",
    "K": "I",
    "L": "G",
    "M": "L",
    "N": "C",
    "O": "E",
    "P": "X",
    "Q": "K",
    "R": "U",
    "S": "N",
    "T": "F",
    "U": "A",
    "V": "M",
    "W": "B",
    "X": "Q",
    "Y": "V",
    "Z": "S",
}

decode_table = {}

for k, v in encode_table.items():
    decode_table[v] = k

print(decode_table)


def encode(str):
    r = ""
    for letter in str:
        r += encode_table[letter]

    return r


def decode(str):
    r = ""
    for letter in str:
        r += decode_table[letter]
    return r


print(encode("GOATS"))
print(encode("ELEPHANT"))

print(decode("JEHFN"))
print(decode("OGOXDHCF"))

