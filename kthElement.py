from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.arrSize = len(nums)
        

        self.heapSort(nums, self.arrSize)
       
        if k == 1:
            return nums[-1]

        if len(nums) < k:
            return nums[-1]

        return nums[(-k)]



    def parentOfElement(self, i: int) -> int:
        return (i/2)

    def leftOfElement(self, i: int) -> int:
        return (2*i+1)

    def rightOfElement(self, i: int) -> int:
        return (2*i+2)

    def maxHeapify(self, nums: List[int], key: int):
        left = self.leftOfElement(key)
        right = self.rightOfElement(key)
        length = self.arrSize

        if left < length and nums[left] > nums[key]:
            largest = left

        else:
            largest = key

        if right < length and nums[right] > nums[largest]:
            largest = right

        if largest != key:
            temp = nums[key]
            nums[key] = nums[largest]
            nums[largest] = temp
            self.maxHeapify(nums, largest)

    def buildMaxHeap(self, nums: List[int], size: int):
        self.arrSize = size
        for index in reversed(range(0,(size//2))):
            self.maxHeapify(nums, index)
            
    def heapSort(self, nums: List[int], size: int):
        self.buildMaxHeap(nums, size)
        
        for i in reversed(range(1, size)):
            temp = nums[0]
            nums[0] = nums[i]
            nums[i] = temp
            self.arrSize = self.arrSize - 1
            self.maxHeapify(nums, 0)

array = [7,6,5,4,3,2,1]
test = Solution()
result = test.findKthLargest(nums=array, k=2)
print(result)


