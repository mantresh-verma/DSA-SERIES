arr = [2,7,11,15]
# arr = [1, 5, 3, 7]
target_sum = 9

# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# approach 1
# T.C. O(n^2) & S.C. O(n)
def find_pair_v1(arr: list, target_sum: int) -> list:
    for i in range(len(arr)):
        curr_sum = 0
        temp_arr = []
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum <= target_sum:
                temp_arr.append(j)
            if curr_sum == target_sum:
                return temp_arr


# When problem said (return indices of the two numbers)
# T.C. O(n^2) & S.C. O(1)
def find_pair_v2(arr: list, target_sum: int) -> list:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target_sum:
                return [i,j]
            

print("Pair:", find_pair_v2(arr, target_sum))