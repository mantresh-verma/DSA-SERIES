arr = [1,2,3,4,5,6]

def reverse_array(arr: list) -> None:
    p1=0
    p2=len(arr)-1
    for _ in range(len(arr)//2):
        temp = arr[p1]                  # bcz python gives tuple unpacking (pythonic way)
        arr[p1] = arr[p2]               # arr[p1], arr[p2] = arr[p2], arr[p1]
        arr[p2] = temp

        p1+=1
        p2-=1


print("Before Reverse arr is: ", arr)
reverse_array(arr)
print("After Reverse arr is: ", arr)