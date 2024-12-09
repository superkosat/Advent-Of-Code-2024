import re

pattern = r'mul\((\d+),(\d+)\)'
instructions = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        instructions.extend(re.findall(pattern, line))


product = 0   
for instruction in instructions:
    product += (int(instruction[0]) * int(instruction[1]))

print(instructions)
print(product)

  
# product = 0
# for instruction in instructions:
#     product += 
        