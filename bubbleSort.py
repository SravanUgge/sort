def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j+1]<nums[j]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                print(nums)

nums=[4,56,2,5,7,9]
sort(nums)
print(nums)