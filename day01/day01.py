import math

with open('input.txt') as input_file:
    input_lines = input_file.read().split('\n')
    input_masses = [int(line) for line in input_lines]


def calc_fuel(masses):
    return [math.floor(mass / 3) - 2 for mass in masses]


total_fuel = calc_fuel(input_masses)
print(sum(total_fuel))


# part two
def remove_negative(masses):
    return list(filter(lambda x: x > 0, masses))


fuel_list = list()
fuel_list.append(total_fuel)
tmp = total_fuel
while tmp:
    tmp = calc_fuel(tmp)
    tmp = remove_negative(tmp)
    fuel_list.append(tmp)

print(sum(sum(fuel_list, [])))
