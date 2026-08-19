# grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
grid = [[1, 3], [2, 2]]


def find_missing_and_repeated_values_v1(grid: list) -> list:
    _map = {}
    count = 0
    for arr in grid:
        for i in arr:
            _map[i] = _map.get(i, 0) + 1
            count += 1

    repeated = None
    actual_sum = 0

    for value, frequency in _map.items():
        if frequency > 1:
            repeated = value

        actual_sum += value

    expected_sum = (count * (count + 1)) // 2
    missing = expected_sum - actual_sum

    return [repeated, missing]

# code cleaning approach
def find_missing_and_repeated_values_v2(grid: list) -> list:
    _map = {}
    count = actual_sum = 0
    repeated = None

    for arr in grid:
        for i in arr:
            _map[i] = _map.get(i, 0) + 1
            if _map[i] > 1:
                repeated = i
            else:
                actual_sum += i
            count += 1

    expected_sum = (count * (count + 1)) // 2
    missing = expected_sum - actual_sum

    return [repeated, missing]

# grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
# I need to understand this solution bcz i copied this from chatgpt to know how to solve in SP. O(1)
def find_missing_and_repeated_values_v3(grid: list) -> list:
    n = len(grid)
    repeated = None

    for r in range(n):
        for c in range(n):
            x = abs(grid[r][c])

            # x ko ek fixed cell se map karo
            idx = x - 1
            target_r = idx // n
            target_c = idx % n

            # already negative => x repeat ho raha hai
            if grid[target_r][target_c] < 0:
                repeated = x
            else:
                grid[target_r][target_c] *= -1

    # Jo cell positive reh gaya, uska number missing hai
    missing = None

    for r in range(n):
        for c in range(n):
            if grid[r][c] > 0:
                missing = r * n + c + 1
                break

    return [repeated, missing]

        


arr = find_missing_and_repeated_values_v3(grid)
print(arr)
