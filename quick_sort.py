# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# First part of quick sort   

arr = [14,60,23,54,70,9,1,3]
pivot = arr[2]
count = 0
i = 0
j = 0

while count < len(arr):
    if arr[j] > pivot:
        while count < len(arr):
            i -= 1
            # print(arr.index(arr[j]), arr.index(arr[i]))
            # print(arr)
            if  arr.index(arr[i]) < arr.index(arr[j]):
                arr[i], arr[arr.index(pivot)] = arr[arr.index(pivot)], arr[i]
                break
            elif arr[i] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                break
    
    if arr[arr.index(pivot)] != pivot:
        break
    
    count += 1
    j += 1
    
print(arr)

# Second part of quick sort

# To be implemented