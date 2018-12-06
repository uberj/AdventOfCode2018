from pprint import pprint
def parking_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def furthest_point(input_):
    coords = list(map(lambda i: list(map(int, i.split(", "))), input_))
    max_x, max_y = -1, -1
    for coord in coords:
        max_x = max(max_x, coord[0] + 2)
        max_y = max(max_y, coord[1] + 2)

    coordinate_grids = [[[None for _ in range(max_x)] for _ in range(max_y)] for _ in range(len(coords))]

    for i, coord in enumerate(coords):
        for y in range(max_y):
            for x in range(max_x):
                coordinate_grids[i][y][x] = parking_distance((x, y), coord)

    best_distance_grid = [[None for x in range(max_x)] for y in range(max_y)]
    for y in range(max_y):
        for x in range(max_x):
            least_distance = 2 ** 32
            for i, candidate_grid in enumerate(coordinate_grids):
                candidate_distance = candidate_grid[y][x]
                if candidate_distance == least_distance:
                    best_distance_grid[y][x] = None
                elif candidate_distance < least_distance:
                    best_distance_grid[y][x] = chr(i + 97)
                    least_distance = candidate_distance

    edge_coords_to_ignore = set(best_distance_grid[0])
    edge_coords_to_ignore = edge_coords_to_ignore.union(set(best_distance_grid[-1]))
    for row in best_distance_grid:
        edge_coords_to_ignore.add(row[0])
        edge_coords_to_ignore.add(row[-1])

    edge_coords_to_ignore = list(filter(lambda x: x is not None, edge_coords_to_ignore))
    flat_bests = []
    for best in best_distance_grid:
        for b in best:
            if b in edge_coords_to_ignore:
                continue
            if not b:
                continue
            flat_bests.append(b)

    all_time_best_count = -1
    for best in set(flat_bests):
        best_count = len(list(filter(lambda x: x == best, flat_bests)))
        if best_count > all_time_best_count:
            all_time_best_count = best_count

    return all_time_best_count


def challenge1():
    with open("inputs/coordinates.txt", "r") as fd:
        return furthest_point(fd.read().strip().split("\n"))


def challenge2():
    with open("inputs/polymer.txt", "r") as fd:
        return furthest_point(fd.read().strip())


if __name__ == "__main__":
    test = furthest_point("""1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split("\n"))
    assert 17 == test, test
    print(challenge1())
    #print(len(challenge2()))
