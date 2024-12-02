file = open('red_nosed_reports.txt').read().splitlines()


def is_all_increasing(data: dict) -> bool:

    for index in range(1, len(data)):
        a = int(data[index-1])
        b = int(data[index])

        if a > b or not is_within_range(a, b):
            return False

    return True


def is_all_decreasing(data: dict) -> bool:

    for index in range(1, len(data)):
        a = int(data[index-1])
        b = int(data[index])

        if a < b or not is_within_range(a, b):
            return False

    return True


def is_within_range(a: int, b: int) -> bool:
    return 1 <= abs(a - b) <= 3


total = 0
for line in file:
    line_array = line.split()

    if is_all_decreasing(line_array) or is_all_increasing(line_array):
        total += 1


print(f'{total} is the number of valid reports')