
def get_size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(get_size(37) == 'S')
# added test to verify size of 38 cms
assert(get_size(38) == 'M')
assert(get_size(40) == 'M')
assert(get_size(43) == 'L')
print("All is well (maybe!)\n")
