import re

pattern = r"\bdo\(\)|\bdon't\(\)|mul\((\d+),(\d+)\)"

with open('input.txt', 'r') as file:
    lines = file.readlines()

text = ''.join(lines)
    
matches = re.finditer(pattern, text)
results = [match.group() for match in matches]
print(results)

answer = 0

pattern = r'mul\((\d+),(\d+)\)'
enabled = True
for operation in results:
    if operation == 'don\'t()':
        enabled = False
    elif operation == 'do()':
        enabled = True
    elif enabled:
        match = re.match(pattern, operation)
        if match:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            answer += (num1 * num2)

print(answer)



