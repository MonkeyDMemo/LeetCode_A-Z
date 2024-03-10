from typing import List
nums1=[9,4,9,8,4]
nums2=[4,9,5]

class Solution:
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)

        return list(set2 & set1)
    
result=Solution.intersection(nums1,nums2)

print(result)