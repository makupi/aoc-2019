import random

with open("input.txt") as input_file:
    input_data = list(map(lambda x: int(x), input_file.read().split(",")))


output = 0
desired = 19690720
seed = [0, 0]
while output != desired:
    data = input_data.copy()
    seed = [random.randint(0, 99), random.randint(0, 99)]
    data[1] = seed[0]
    data[2] = seed[1]

    opc = data[0]
    op_index = 0
    inc = 4
    while opc != 99:
        loc_val1 = data[op_index + 1]
        loc_val2 = data[op_index + 2]
        loc_str = data[op_index + 3]
        val1 = data[loc_val1]
        val2 = data[loc_val2]
        if opc == 1:  # add
            data[loc_str] = val1 + val2
        elif opc == 2:  # mul
            data[loc_str] = val1 * val2
        else:
            raise Exception
        op_index += inc
        opc = data[op_index]

    output = data[0]

print(100 * seed[0] + seed[1])
