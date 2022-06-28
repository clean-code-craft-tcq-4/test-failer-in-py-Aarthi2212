
def get_size(cms):
    size = None   
    if cms >= 36 and cms < 38:
        size = 'S'
    elif cms >= 38 and cms < 42:
        size = 'M'
    elif cms >=42 and cms < 44:
        size = 'L'
    return size


assert(get_size(37) == 'S')
# added test to verify size of 38 cms
assert(get_size(38) == 'M')
assert(get_size(40) == 'M')
assert(get_size(42) == 'L')
assert(get_size(41) == 'M')
# added test to verify zero and negative values
assert(get_size(0) == None)
assert(get_size(-1) == None)
assert(get_size(100) == None)
assert(get_size(43) == 'L')
print("All is well (maybe!)\n")
