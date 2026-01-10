# 
# --------- TWO SUM PATTERN
# 
# def twoSum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         needed = target - num
#         if needed in seen:
#             return [ seen[needed],i]
#         seen[num] = i
#     return []

# nums = [2, 7, 11,15]
# target = 18
# print(twoSum(nums,target))

#  in this code we are using a dict to store the numbers we have seen and when we find the needed number we return to the seen dict and check id it exists means we have found the pair which adds up to target


# --------- MISSING NUMBER PATTERN

# def missNum(nums):
#     n = len(nums)
#     exp_sum = (n*(n+1))//2
#     act_sum = sum(nums)
#     return exp_sum - act_sum

# nums = [3,0,1]
# print(missNum(nums))


# in this code we are calculating the exp_sum of n numbers using formula n(n+1)/2 and then we are calculating sum of given numbers sums(nums) and we return its difference exp_sum - act_sum 







