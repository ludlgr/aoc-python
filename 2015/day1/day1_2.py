floor = 0
step = 0

with open("input", "r") as my_input:
    inst = my_input.read()

while floor >= 0:
    step += 1
    if inst[step-1] == "(":
        floor += 1
    else:
        floor -= 1


print(step)
