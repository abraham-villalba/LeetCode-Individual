class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        max_occurences = max(freq.values())
        output = [[] for _ in range(max_occurences)]
        for num, n_times in instances.items():
            # Add each num or element to it's corresponding row
            for i in range(n_times):
                output[i].append(num)
        return output
        



