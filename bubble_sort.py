arr = [5,4,3,2,1]
result = []

for i in range(len(arr)):
    for j in range(len(arr)):
        sub_arr = arr[j : j + 2]
        if len(sub_arr) < 2:
            break
        if sub_arr[1] < sub_arr[0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        result.append(arr[:])


print("States ", result)
print("====================>")
print("Sorted Array", arr)
