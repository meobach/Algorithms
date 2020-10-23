#def twoSum(self, nums, target):
def twoSum(nums, target):

    if(target%2==0):
        count=0
        arr=[]
        half_target=int(target/2)
        for i,item in enumerate(nums):
            if(item==half_target):
                count+=1
                arr.append(i)
        if(count==2):
            return arr
    index_list=dict()
    for i,item in enumerate(nums):
        index_list[item]=i
    sorted_nums=sorted(nums)
    i,j=0,len(sorted_nums)-1
    total=sorted_nums[i]+sorted_nums[j]
    while(True):
        if(total<target):
            total-=sorted_nums[i]
            i+=1
            total+=sorted_nums[i]
        else:
            if(total>target):
                total-=sorted_nums[j]
                j-=1
                total+=sorted_nums[j]
            else:
                return [index_list[sorted_nums[i]],index_list[sorted_nums[j]]]
print(twoSum([3,2,4],6))

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]