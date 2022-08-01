def shuffle(nums, n):
  res=[]
  for i in range(n):
    res.append(nums[i])
    res.append(nums[n+i])
  return res
s=[2,5,1,3,4,7]
r=shuffle(s,3)
print(r)