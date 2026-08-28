class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        singles = set()
        for d in nums:
            if d in singles:
                return True
            else:
                singles.add(d)
        return False   