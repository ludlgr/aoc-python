def get_houses(directions):
    current_pos = (0, 0)
    houses = set()
    houses.add(current_pos)


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

    return houses


with open("input", "r") as my_input:
    directions = my_input.read()

santa_moves = [directions[i] for i in range(len(directions)) if i % 2 == 0]
robot_moves = [directions[i] for i in range(len(directions)) if i % 2 != 0]

santa_houses = get_houses(santa_moves)
robot_houses = get_houses(robot_moves)
houses = santa_houses.union(robot_houses)

print(len(houses))
