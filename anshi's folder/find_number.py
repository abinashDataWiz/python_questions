nums = [2,3,4,5,6,7,8,9,]

target = 3

# Print out the index of the target in nums using a for loop

# for i in range (len(nums)):
#  if nums[i] == 5:
#     print(i)

i = 0

while i < len(nums) and nums[i] != target:
     i = i + 1
if i < len(nums):
     print(i)
