nums=[1,2,3,4]
it=iter(nums)

print(it.__next__())
print(next(it))
for i in nums:
    print(i)
print(it.__next__())


