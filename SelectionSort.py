def Sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in  range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        print(nums)

nums=[9,8,7,6,5,4,3]
Sort(nums)
print(nums)