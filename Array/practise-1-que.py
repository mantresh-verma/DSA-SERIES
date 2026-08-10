arr = [1, 2, 1, 4, 2, 6, 3, 4]

# WAF to calculate sum & product of all numbers in an array.
# WAF to swap the min and max number of an array.
# WAF to print intersection of 2 array.

# ==============================================================================================================
# WAF to print all the unique values in an array.
# Approach 1
# T.C., O(n^2) & S.P., O(1)
def print_unique_val_in_arr(arr: list) -> None:
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            print(arr[i], end=" ")


# Approach 2
# T.C., O(n) & S.P., O(n)
def print_unique_val_in_arr_using_hashmap(arr: list) -> None:
    _map = {}
    for i in range(len(arr)):
        _map[arr[i]] = _map.get(arr[i], 0) + 1

    for key, val in _map.items():
        if val == 1:
            print(key, end=" ")

# Approach 3 (Sorting e.g., Merge sort)
# T.C., O(n log n) & S.P., O(1)
def print_unique_val_in_arr_using_sort(arr: list) -> None:
    pass


# ==============================================================================================================

print_unique_val_in_arr_using_hashmap(arr)
