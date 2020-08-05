def letter_count(s):

    d = {}

    for letter in s:
        if letter.isspace():
            continue
        letter = letter.lower()

        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d


def print_sorted_letter_count(s):
    d = letter_count(s)

    items = list(d.items())
    items.sort(key=lambda e: e[1], reverse=True)

    for i in items:
        print(f"{i[0]}: {i[1]}")


# print_sorted_letter_count(
#     "they also thought in the 1980s that there would be flying cars by 2015, from Back to the Future 2"
# )

print_sorted_letter_count(
    "For expensive operations, caching the results in a lookup table speeds future queries.The lookup table can be built in advance by iterating over all values in the domain of the function and recording the results.Or, more lazily, can be build as the individual values are passed in. Modify the code in this directory to build a lookup table so that it can finish running in under a minute. There's no test file for this. It's counting to 50,000, so if it finishes before you give up, then you're golden."
)

