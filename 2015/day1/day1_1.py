floor = 0

with open("input", "r") as my_input:
    inst = my_input.read()

for char in inst:
    if char == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
