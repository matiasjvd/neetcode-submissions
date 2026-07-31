class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        drops = []
     
        numbers_reps = []


        for number in nums:
            if number not in drops:

                numbers_reps.append([number, nums.count(number)])
                drops.append(number)
                
        numbers_reps = sorted(numbers_reps, key=lambda lista: lista[1], reverse=True)

        output = [lista[0] for lista in numbers_reps][:k]
        print(output)

        return output

            

        