# b = "beej".encode()
# for letter in b:
#     print(letter)

HASH_DATA_SIZE = 8

hash_data = [None] * HASH_DATA_SIZE


class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def hash_function(str):
    # Naive hashing function -- do not use in production
    bytes_list = str.encode()

    total = 0

    for b in bytes_list:  # O(n) over the length of the key
        total += b
        # Optional (but correct) forcing the result to a certain number of bits
        # total &= 0xFFFFFFFF  # 32 bits (8 f's)
        # total &= 0xFFFFFFFFFFFFFFFF  # 64 bits (16 f's)

    return total


def get_index(str):
    hash_value = hash_function(str)
    return hash_value % HASH_DATA_SIZE


def put(k, v):
    # 'for a given key, store a value in the hash table'
    print(f"Putting {k}, {v}")
    index = get_index(k)

    if hash_data[index] is not None:
        print("COLLISION!!")

    # hash_data[index] = v
    hash_data[index] = HashTableEntry(k, v)


def get(k):
    index = get_index(k)
    return hash_data[index]


def delete(k):
    index = get_index(k)
    hash_data[index] = None


# print(hash_data)
put("Beej!", "hello world!")
put("g", 3490)
# print(hash_data)
# put("Beej!", "hello, again")
# print(hash_data)

print(get("Beej!"))
# print(get("g"))

