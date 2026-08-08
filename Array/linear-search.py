def linear_search(arr: list, targate: int) -> int | None:
    found = None
    for i in range(len(arr)):
        if arr[i] == targate:
            found = arr[i]

    if found != None:
        return found
    else:
        print("Targated Element didn't Find!!")


arr = list(map(int, input("Enter Array: ").split()))
targate = int(input("Enter Targate Element: "))

print("Result: ", linear_search(arr, targate))