import math


total_ribbon = 0

with open("input", "r") as my_input:
    for box in my_input:
        dims = box.split("x")
        dims = [int(dim) for dim in dims]
        dims.sort()
        ribbon = 2*dims[0] + 2*dims[1] + math.prod(dims)

        total_ribbon += ribbon

print(total_ribbon)
