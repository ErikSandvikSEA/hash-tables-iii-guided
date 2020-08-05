d = {"foo": 12, "bar": 17, "qux": 2}

items = list(d.items())

items.sort()
print(items)


def fun1(e):
    print(e)
    return e[1]


items.sort(key=fun1)

print(items)


# first get the items in a hash table as tuples
# then we can sort
