nums = [7, 5, 9, 2, 8]

result = []

for i in range(0, len(nums)):
    mini = nums[i]
    for j in range(i, len(nums)):
        if nums[j] < mini:
            mini = nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        # print(nums)
        result.append(nums)
    # print(result[0])


print("States ", result)
print("==================>")
print("Sorted array", nums)
