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


def get_separator_index(color_manual):
    all_color_separator_indices = []
    for color_map in color_manual:
        indices = [i for i, c in enumerate(color_map) if c == "|"]
        all_color_separator_indices.append(indices)
    return all_color_separator_indices

result = print_color_map()
assert(result == 25)
color_mapping = get_color_map()
assert(color_mapping.get(1) == ["White", "Blue"])
assert(next(iter(color_mapping)) == 1)
color_manual = format_color_mapping()

assert(len(set(tuple(x) for x in get_separator_index(color_manual))) == 1)

print("All is well (maybe!)\n")
