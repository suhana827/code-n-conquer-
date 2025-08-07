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



