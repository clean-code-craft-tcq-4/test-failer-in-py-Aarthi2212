major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_map():
    color_mapping = {}
    for i, major_color in enumerate(major_colors):
        for j, minor_color in enumerate(minor_colors):
            color_mapping.update({i * 5 + j: [major_color, minor_color]})
    return color_mapping

def format_color_mapping():
    color_mapping = get_color_map()
    color_manual = []
    for pair_number, color_pairs in color_mapping.items():
        major_color, minor_color = color_pairs
        color_manual.append(f'{pair_number} | {major_color} | {minor_color}')
    return color_manual

def print_color_map():
    color_manual = format_color_mapping()
    for color_map in color_manual:
        print(color_map)
    return len(color_manual)


def get_indices_of_separator(color_manual):
    separator_indices_of_all_pairs = []
    separator = "|"
    for color_map in color_manual:
        indices = [i for i, c in enumerate(color_map) if c == separator]
        separator_indices_of_all_pairs.append(indices)
    return separator_indices_of_all_pairs

result = print_color_map()
# test total set of pairs
assert(result == 25)

color_mapping = get_color_map()

# test if pair_numbers are zero based
assert(color_mapping.get(1) == ["White", "Blue"])

# test if pair number starts with 1
assert(next(iter(color_mapping)) == 1)

color_manual = format_color_mapping()

# check if the separators are aligned in a same position by checking index of separators.
assert(len(set(tuple(x) for x in get_indices_of_separator(color_manual))) == 1)

print("All is well (maybe!)\n")
