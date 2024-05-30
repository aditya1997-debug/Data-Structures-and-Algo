arr = [13,46,24,52,20,9]

states = []

for index, i in enumerate(arr):
    sub_arr = arr[:index]
    count = len(arr[:index])
    while count > 0:
        # print(sub_arr, arr[index], sub_arr[count - 1], arr[count - 1])
        if arr[index] < arr[count - 1]:
            arr[index], arr[count - 1] = arr[count - 1], arr[index]
            states.append(arr[:])
        count -= 1
        index -= 1
        
print(states)
print("=================>")
print("Sorted array", states[-1])