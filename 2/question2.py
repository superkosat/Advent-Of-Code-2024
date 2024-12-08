from question1 import is_safe

with open('input.txt', 'r') as file:
    lines = file.readlines()

def is_safe_dampener(lst):
    n = len(lst)
    
    for i in range(n):
        mod_lst = lst[:i] + lst[i + 1:]
        if is_safe(mod_lst):
            return True
    
    return False


safe = 0
for line in lines:
    nums = line.split(' ')
    nums = list(map(int, nums))
    if is_safe_dampener(nums): safe += 1

print(safe)