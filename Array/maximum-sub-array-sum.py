arr = [1, 2, 1, 4, 2, 6]
arr = [-1, -2, -3]


# Using Brute Force Approach
# T.C. O(n^2) & S.C O(n)
def find_maximum_subarray_sum_v1(arr: list):
    max_sum = float("-inf")
    sub_arr = []
    for i in range(len(arr)):
        current_sum = 0
        temp_arr = []
        for j in range(i, len(arr)):
            current_sum += arr[j]
            temp_arr.append(arr[j])

            if max_sum < current_sum:
                max_sum = current_sum
                sub_arr = temp_arr[:]

    return max_sum, sub_arr


# approach 2
# T.C. O(n) & S.C O(1)
def find_maximum_subarray_sum_v2(arr: list):
    curr_sum = max_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if max_sum < curr_sum:
            max_sum += arr[i]

    return max_sum


# approach 3
# Kadane's Algorithm
# # T.C. O(n) & S.C O(1)
def find_maximum_subarray_sum_v3(arr: list):
    max_sum = float("-inf")
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if max_sum < curr_sum:
            max_sum = curr_sum
        
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


max_sum = find_maximum_subarray_sum_v3(arr)
print(max_sum)
