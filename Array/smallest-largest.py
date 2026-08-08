# WAP to find the smallest and largest number in Array.
def find_smallest_largest(arr: list) -> int:
    largest = smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
        if arr[i] > largest:
            largest = arr[i]

    return (smallest, largest)


arr = list(map(int, input("Enter array: ").split()))

smallest, largest = find_smallest_largest(arr)

print("smallest value: ", smallest)
print("largest value: ", largest)
