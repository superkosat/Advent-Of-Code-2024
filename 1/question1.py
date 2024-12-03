col1, col2 = [], []

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    col1.append(int(lines[i].split()[0]))
    col2.append(int(lines[i].split()[1]))

col1.sort()
col2.sort()

difference = sum(abs(x - y) for (x, y) in zip(col1, col2))

print(difference)