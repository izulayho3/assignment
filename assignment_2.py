ribbon = int(input("Enter the number of ribbons: "))


def ribbon1(ribbon_length):
    if ribbon_length < 78:
        return "Below range"
    elif 78 <= ribbon_length <= 82:
        return "In range"
    else:
        return "Above range"


total = 0
below_range = 0
inrange = 0
above_range = 0
for i in range(ribbon):
    ribbon_length = int(input("Enter the ribbon length: "))
    total += ribbon_length
    box = ribbon1(ribbon_length)
    print(box)
    if box == "Below range":
        below_range += 1
    elif box == "In range":
        inrange += 1
    else:
        above_range += 1


def average(total, ribbon):
    return total/ribbon


average_length = average(total, ribbon)
print(f"Total lenght: {total} mm")
print(f"Average length: {average_length} mm")
print(f"Below range: {below_range}")
print(f"In range: {inrange}")
print(f"Above range: {above_range}")
