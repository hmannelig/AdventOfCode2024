file = open("locations_ids_list.txt").read().splitlines()

left_locations = []
right_locations = []
for line in file:
    locations = line.split()
    left_locations.append(locations[0])
    right_locations.append(locations[1])


# Custom sorting algorithm. Not the most efficient or prettiest
# but wanted to code it myself
def sort_ascending(data: dict) -> dict:
    sorted_list = []
    for index in range(len(data)):
        location = data[index]

        if len(sorted_list) == 0:
            sorted_list.append(location)

        else:
            inner_index = 0
            while inner_index < len(sorted_list) and location > sorted_list[inner_index]:
                inner_index += 1

            sorted_list.insert(inner_index, location)

    return sorted_list


# INFO: getting the absolute difference without using abs()
def calculate_distance(first_location, second_location) -> int:
    return (first_location - second_location) if first_location > second_location else second_location - first_location


# FIRST PART SOLUTION
def sum_total_distances() -> int:
    sorted_left_locs = sort_ascending(left_locations)
    sorted_right_locs = sort_ascending(right_locations)

    total_distance = 0
    n = len(sorted_left_locs)
    for i in range(0, n):
        total_distance += calculate_distance(int(sorted_left_locs[i]), int(sorted_right_locs[i]))

    return total_distance


print(f" {sum_total_distances()} is the sum of total distances")


# SECOND PART SOLUTION
def count_occurrence(location_id, data: dict) -> int:
    total = 0
    for n in data:
        if location_id == n:
            total += 1

    return total


def calculate_similarity() -> int:
    recorded_locs = {}
    total_similarity = 0
    for n in left_locations:
        if n not in recorded_locs:
            recorded_locs[n] = count_occurrence(n, right_locations)

        total_similarity += (int(n) * int(recorded_locs[n]))

    return total_similarity


print(f" {calculate_similarity()} is the sum of total similarity distances")
