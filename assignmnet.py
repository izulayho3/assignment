def replace_value(values, index, new_value):
    values[index] = new_value
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
def summarize(values):
    return min(values), max(values), sum(values)
days = int(input("Enter the number of days: "))
original = []
for i in range(days):
    time = int(input("Enter typing practice time in minutes: "))
    original.append(time)
updated = original[:]
idx_to_correct = int(input("Enter the index to correct: "))
new_time = int(input("Enter the new practice time: "))
replace_value(updated, idx_to_correct, new_time)
target = int(input("Enter the practice time to search for: "))
first_idx = find_first(updated, target)
match_count = updated.count(target)
minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum practice time: {minimum} minutes")
print(f"Maximum practice time: {maximum} minutes")
print(f"Total practice time: {total} minutes")
if first_idx != -1:
    print(f"First matching index: {first_idx}")
else:
    print("Target not found")
print(f"Matching values: {match_count}")
