col1, col2 = [], []

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    col1.append(int(lines[i].split()[0]))
    col2.append(int(lines[i].split()[1]))

mp = {}

for num in col2:
    if num not in mp:
        mp[num] = 1
    else:
        mp[num] += 1

similarity = 0
for num in col1:
    if num in mp:
        similarity += num * mp[num]

print(similarity)

