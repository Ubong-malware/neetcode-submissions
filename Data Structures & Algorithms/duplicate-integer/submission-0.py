class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for num in nums:
            if num in freq: #number exists in dictionary?
                return True
            freq[num] = 1  #adding to the dictionary, if not exist
        
        return False
            