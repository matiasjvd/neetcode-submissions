class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            nums_2 = nums.copy()

            valor = nums_2.pop(i)
            suspect = target - valor

            if suspect in nums_2:
                indice = nums_2.index(suspect)

                if indice >= i:
                    indice += 1

                return sorted([i, indice])

        return []
        
        