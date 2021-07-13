class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i in range(len(citations)):
            if citations[i]>=len(citations)-i:
                return len(citations)-i
        return 0
    
#Time compleixty O(n) and Space complexity O(1)