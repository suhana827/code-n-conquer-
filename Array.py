# Given an array of integers, return true if any value appears
# at least twice in the array, else return false.

# def findNum():
#     for i in range(len(arr)):
#         for j in range(i+1,(len(arr))):
#             if arr[i] == arr[j]:
#                 return "true",arr[i]
            
#     return "false"

# arr = [1,2,3,3,5]
# print(findNum())


# Find the index of the first occurrence of a target number in a sorted 
# array using Binary Search. If not found, return -1.


# def indexFinder(nums,target):
#     left = 0
#     right = len(nums)-1

#     while left <= right:
#         mid = (left+right)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# nums = [1,2,3,4,5,6,7]
# target = 5
# print(indexFinder(nums,target))



# You are given two sorted arrays. Merge them into one 
# sorted array(without using sort function).

# def sort_array(arr1,arr2):
#     arr3 = []
#     i = 0
#     j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr3.append(arr1[i])
#             i += 1
#         else:
#             arr3.append(arr2[j])
#             j += 1

#     while i < len(arr1):
#         arr3.append(arr1[i])
#         i += 1

#     while j < len(arr2):
#         arr3.append(arr2[j])
#         j += 1

#     return arr3
  

# arr1 = [1,2,3]
# arr2 = [4,5,6]
# print(sort_array(arr1,arr2))



#  Return the second largest number in the array. If it doesn't exist, return null.

# def second_largest(arr):
#     largest = 0
#     second = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):  
#             if arr[i] > arr[j]:
#                 if arr[i] > largest:
#                     second = largest
#                     largest = arr[i]
#                 elif arr[i] > second and arr[i] != largest:
#                     second = arr[i]
#             else:
#                 if arr[j] > largest:
#                     second = largest
#                     largest = arr[j]
#                 elif arr[j] > second and arr[j] != largest:
#                     second = arr[j]
#     return second if second != 0 else None


# arr = [1, 4, 2, 6, 7,7]
# print(second_largest(arr))  

    
# Two Sum Problem
# Given an array of integers nums and an integer target, return the indices 
# of the two numbers such that they add up to target.


# def twoNum(nums,target):
#     pairs = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 pairs.append((nums[i], nums[j]))
            
#     return pairs

# nums = [2,3,5,4,1]
# target = 5
# print(twoNum(nums,target))   


# Reversing an array
# nums = [2,4,7,3,5,8]
# reverse_nums = []
# i = len(nums)-1
# while i >= 0:
#     reverse_nums.append((nums[i]))
#     i -= 1
# print(reverse_nums)


# Move Zeros to End
# Write a function that moves all 0's to the end of an array while 
# maintaining the relative order of the non-zero elements.

# def zeroes(arr):
#     i = 0  
#     for j in range(len(arr)): 
#         if arr[j] != 0:
#             arr[i] = arr[j]
#             i += 1
#     while i < len(arr):
#         arr[i] = 0
#         i += 1

#     return arr

# arr = [2, 0, 3, 4, 0, 1, 6, 7, 0]
# print(zeroes(arr))
