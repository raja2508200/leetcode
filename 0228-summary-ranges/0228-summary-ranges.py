class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
    
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            print(nums[i],nums[i-1] + 1)
            
            if nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")
                start = nums[i]
        
        # Handle the last range
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        return ranges
            