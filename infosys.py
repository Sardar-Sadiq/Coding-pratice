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



# ------- TWO-POINTER / MOVE IN PLACE SHUFFLE
# def moveZeroes(nums):
#     pos = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[pos], nums[i] = nums[i], nums[pos]
#             pos += 1
#     return nums

# nums = [0,1,0,3,12]
# print(moveZeroes(nums))

# in this code we are using two pointers one to traverse the array and other to keep tracck of position to place non zero elements and we swap them when we find non zero element




#------ unique character in a string

# def fir_Uniq_Ch(s):
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char,0)+1
#     for i in range(len(s)):
#         if counts[s[i]] ==1:
#             return i 
#     return -1


# print(fir_Uniq_Ch("aabcd"))    # Returns 2 (first unique char is 'b')
# print(fir_Uniq_Ch("infosys"))  # Returns 0 (first unique char is 'i')
# print(fir_Uniq_Ch("aaa"))      # Returns -1 (no unique characters)


# in this code we are using a dict to count of each character in the string and then we find the character with count 1 and return its index if no unique character found we return -1









# ------- Anagram Grouping


# from collections import defaultdict
# def anagram(strs):
#     groups = defaultdict(list)
#     for s in strs:
#         sorterd_key = "".join(sorted(s))
#         groups[sorterd_key].append(s)
#     return list(groups.values())

# strs = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
# print(anagram(strs))

# in this code we are using a dict to group the anagrams by using sorted strs as key and appending to OG strs to the dict values and finally returning the values of the dict as list of lists





# rpg game

# def max_mon(n, ini_exp,power,bonuses):
#     monsters = sorted(zip(power, bonuses))
#     count = 0
#     curr_exp = ini_exp
#     for p, b in monsters:
#         if curr_exp >= p:
#             curr_exp +=b
#             count +=1
#         else:
#             break
#     return count

# exp = 10 
# n =2
# power = [20,5]
# bonuses = [5,2]
# print(max_mon(n,exp,power,bonuses))



# -------- Frequency Sort


# from collections import Counter

# def freq(nums):
#     counts = Counter(nums)
#     nums.sort(key=lambda x: (counts[x], x))
#     return nums

# nums = [4,4,1,2,2,3,3,3]
# print(freq(nums))  

# in this code we are using counter to count the frequency of each number and then sorting the nums based on frequency and then by number itself in ascending order using lambda function as key in sort method


# --------- Equilibrium Index

# def findEquil(nums):
#     tot_sum = sum(nums)
#     lef_sum = 0
#     for i,x in enumerate(nums):
#         if lef_sum == (tot_sum - lef_sum -x):
#             return i 
#     return -1 

# nums = [1,7,3,6,5,6]
# print(findEquil(nums))

# in this code we are calculating total sum of array and then iterating through the array and checking if left sum is equal to right sum by subtracting left sum and current element from total sum if found we return index else -1