
with open('input.txt', 'r') as file:
    lines = file.readlines()

def is_safe(lst):
    inc = True
    dec = True
    dampener = False

    for i in range(1, len(lst)):
        diff = lst [i] - lst[i - 1]

        if diff <= 0 or diff > 3:
            inc = False

        if diff >= 0 or diff < -3:
            dec = False

        if diff == 0:
            return False
        
    return inc or dec

safe = 0
for line in lines:
    nums = line.split(' ')
    nums = list(map(int, nums))
    if is_safe(nums): safe += 1

print(safe)
