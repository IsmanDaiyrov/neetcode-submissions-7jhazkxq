class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        res = []

        for i, n in enumerate(nums2):
            map[n] = i
        
        for n in nums1:
            res.append(map[n])
            
        return res