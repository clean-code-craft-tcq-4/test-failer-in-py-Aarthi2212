''' Tests to verify color mapping'''
from color_mapper import print_color_map, get_color_map, format_color_mapping, get_indices_of_separator

# test total set of pairs with varying length
major_colors = ["White", "Red", "Black"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
result = print_color_map(major_colors, minor_colors)
assert(result == 15)

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange"]
result = print_color_map(major_colors, minor_colors)
assert(result == 10)

major_colors = ["White", "Red", "Black"]
minor_colors = ["Blue", "Orange"]
result = print_color_map(major_colors, minor_colors)
assert(result == 6)

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
result = print_color_map(major_colors, minor_colors)
assert(result == 25)

color_mapping = get_color_map(major_colors, minor_colors)

# test if pair_numbers are zero based
assert(color_mapping.get(1) == ["White", "Blue"])

# test if pair number starts with 1
assert(next(iter(color_mapping)) == 1)

color_manual = format_color_mapping()

# check if the separators are aligned in a same position by checking index of separators.
assert(len(set(tuple(x) for x in get_indices_of_separator(color_manual))) == 1)

print("All is well (maybe!)\n")
