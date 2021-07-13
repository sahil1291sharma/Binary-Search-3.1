class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)-1
        
        while high >= low:
            mid = low + (high - low) //2
            if len(citations) - mid == citations[mid]:
                return len(citations) - mid 
            elif len(citations) - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return len(citations) - low
    
#Time complexity O(logN) where N is number of elements in citations array
#Space complexity is O(1)