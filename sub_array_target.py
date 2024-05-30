# Code for finding sub array where sum of sub array is equal to target
arr = [1,8,3,5,5,5,6,4,8,9,2,4,4,5]
target = 15

sum_ = 0
index = 0

for i in range(len(arr)):
    for j in range(index, len(arr)):
        sum_ += arr[j]
        # print(sum_)
        if sum_ > target:
            # print(index)
            sum_ = 0
            index += 1
            break
        elif sum_ == target:
            print(sum_, arr[index : j + 1])