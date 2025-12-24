def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid      
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1   

arr = [2, 5, 8, 12, 16, 23, 38]
x = 16
result = binary_search(arr, x)
print("Element found at index:", result)
