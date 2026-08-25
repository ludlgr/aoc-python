total_paper = 0

with open("input", "r") as my_input:
    for box in my_input:
        dims = box.split("x")
        dims = [int(dim) for dim in dims]
        sides = [dims[0]*dims[1], dims[1]*dims[2], dims[2]*dims[0]]
        paper = 2*sides[0]+ 2*sides[1]+ 2*sides[2] + min(sides)

        total_paper += paper

print(total_paper)
