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

def sort_array(arr1,arr2):
    arr3 = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] > arr2[j]:
                arr3.append(arr2[j])
            else:
                arr3.append(arr1[i])
                
               
    return(arr3)

arr1 = [1,2,3]
arr2 = [4,5,6]
print(sort_array(arr1,arr2))