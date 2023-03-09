from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    listLen = len(nums)
    result = []
    for i in range(0, listLen):
        for j in range(i + 1, listLen):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result
