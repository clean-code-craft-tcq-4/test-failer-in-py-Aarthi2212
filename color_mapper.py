''' Maps Colors with pair numbers '''

def get_color_map(major_colors, minor_colors):
    color_mapping = {}
    for i, major_color in enumerate(major_colors):
        for j, minor_color in enumerate(minor_colors):
            color_mapping.update({i * 5 + j: [major_color, minor_color]})
    return color_mapping

def format_color_mapping(major_colors, minor_colors):
    color_mapping = get_color_map(major_colors, minor_colors)
    color_manual = []
    for pair_number, color_pairs in color_mapping.items():
        major_color, minor_color = color_pairs
        color_manual.append(f'{pair_number} | {major_color} | {minor_color}')
    return color_manual

def print_color_map(major_colors, minor_colors):
    color_manual = format_color_mapping(major_colors, minor_colors)
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