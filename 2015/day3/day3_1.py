current_pos = (0, 0)
houses = set()
houses.add(current_pos)

with open("input", "r") as my_input:
    directions = my_input.read()

for move in directions:
    if move == ">":
        current_pos = (current_pos[0]+1, current_pos[1])
    elif move == "<":
        current_pos = (current_pos[0]-1, current_pos[1])
    elif move == "^":
        current_pos = (current_pos[0], current_pos[1]+1)
    elif move == "v":
        current_pos = (current_pos[0], current_pos[1]-1)
    houses.add(current_pos)

print(len(houses))
