
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
assert(get_size(42) == 'L')
assert(get_size(41) == 'M')
assert(get_size(36) == 'XS')
# added test to verify zero and negative values
assert(get_size(0) == None)
assert(get_size(-1) == None)
assert(get_size(43) == 'L')
print("All is well (maybe!)\n")
