class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        singles = set()
        odd = set()
        for d in nums:
            if d in singles:
                odd.add(d)
            else:
                singles.add(d)
        if len(odd) > 0:
            return True
        else:
            return False   