def findClosestNumber(nums):
        out = nums[0]
        for i in nums:
            if i == abs(out):
                out = i
            elif abs(i) < abs(out):
                out = i
        return out 

closest_num = findClosestNumber([-4,-2,1,4,8])
print(closest_num) 