''' Maps Colors with pair numbers '''
manual_format = '{:<{width}} | {:<{width}} | {:<{width}}'

def get_color_map(major_colors, minor_colors):
    total_pairs = len(major_colors) * len(minor_colors)
    color_mapping = {}
    for pair_number in range(1, total_pairs + 1):
        zero_based_pair_number = pair_number - 1
        major_color_index = zero_based_pair_number // len(minor_colors)
        minor_color_index = zero_based_pair_number % len(minor_colors)
        major_color, minor_color = major_colors[major_color_index], minor_colors[minor_color_index]
        color_mapping.update({pair_number : [major_color, minor_color]})
    return color_mapping

def format_color_mapping(major_colors, minor_colors):
    color_mapping = get_color_map(major_colors, minor_colors)
    color_manual = []
    for pair_number, color_pairs in color_mapping.items():
        major_color, minor_color = color_pairs
        color_manual.append(manual_format.format(pair_number, major_color, minor_color, width=11))
    return color_manual

def print_color_map(major_colors, minor_colors):
    color_manual = format_color_mapping(major_colors, minor_colors)
    print(manual_format.format("Pair number", "Major color", "Minor color", width=11))
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