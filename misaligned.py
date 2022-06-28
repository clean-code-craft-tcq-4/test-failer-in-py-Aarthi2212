''' Tests to verify color mapping'''
from color_mapper import print_color_map, get_color_map, format_color_mapping, get_indices_of_separator, get_color_from_index

# test total set of pairs with varying length
major_colors = ["White", "Red", "Black"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
result = print_color_map(major_colors, minor_colors)
assert(result == 15)


color_mapping = get_color_map(major_colors, minor_colors)
assert(color_mapping.get(5) == ["White", "Slate"])
assert(color_mapping.get(11) == ["Black", "Blue"])

assert(get_color_from_index(major_colors, 0) == "White")

error = ""
try:
    result = get_color_from_index(minor_colors, 6)
except Exception as e:
    result = e
    error = str(e)
assert(isinstance(result, Exception) == True)
assert(error == "Color index out of range")

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange"]
result = print_color_map(major_colors, minor_colors)
assert(result == 10)

color_mapping = get_color_map(major_colors, minor_colors)
assert(color_mapping.get(3) == ["Red", "Blue"])
assert(color_mapping.get(8) == ["Yellow", "Orange"])

major_colors = ["White", "Red", "Black"]
minor_colors = ["Blue", "Orange"]
result = print_color_map(major_colors, minor_colors)
assert(result == 6)

color_mapping = get_color_map(major_colors, minor_colors)
assert(color_mapping.get(3) == ["Red", "Blue"])
assert(color_mapping.get(5) == ["Black", "Blue"])
assert(color_mapping.get(6) == ["Black", "Orange"])

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
result = print_color_map(major_colors, minor_colors)
assert(result == 25)

color_mapping = get_color_map(major_colors, minor_colors)

# test if pair_numbers are zero based
assert(color_mapping.get(1) == ["White", "Blue"])

assert(color_mapping.get(4) == ["White", "Brown"])

assert(color_mapping.get(5) == ["White", "Slate"])

assert(color_mapping.get(6) == ["Red", "Blue"])

assert(color_mapping.get(10) == ["Red", "Slate"])

assert(color_mapping.get(11) == ["Black", "Blue"])

assert(color_mapping.get(16) == ["Yellow", "Blue"])

assert(color_mapping.get(18) == ["Yellow", "Green"])

assert(color_mapping.get(21) == ["Violet", "Blue"])

assert(color_mapping.get(25) == ["Violet", "Slate"])

# test if pair number starts with 1
assert(next(iter(color_mapping)) == 1)

color_manual = format_color_mapping(major_colors, minor_colors)
# check if the separators are aligned in a same position by checking index of separators.
assert(len(set(tuple(x) for x in get_indices_of_separator(color_manual))) == 1)

print("All is well (maybe!)\n")
