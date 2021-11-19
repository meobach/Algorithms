class Arr:
    def __init__(self,item) -> None:
        self.length=len(item)
        self.arr=item
    def reverse(self):
        for i in range(int(self.length/2)):
            temp=self.arr[i]
            self.arr[i]=self.arr[self.length-i-1]
            self.arr[self.length-i-1]=temp
        return self.arr
    def prefix_sum_circular_arr(self):
        circular_arr=self.arr+self.arr
        prefix_sum=[]
        current_sum=0
        prefix_residual=0
        for i in range(self.length*2):
            current_sum+=circular_arr[i]
            prefix_sum.append(current_sum)
        count=0
        print(prefix_sum)
        i=0
        while(i<self.length):
            for j in range(i,i+self.length):
                if(count==self.length):
                    return i
                else:
                    if(prefix_sum[j]-prefix_residual>=0):
                        count+=1
                    else:
                        prefix_residual=prefix_sum[j]
                        count=0
                        i=j+1
                        break

        return -1
    def maximum_product_length_string(self,str):
        return str
    def minimize_flip_k_length_subarr(self,arr):
        return arr
    def num_sub_arr_even_product(self,arr):
        #for i in range(len(arr)):
        return arr
    
        #print(arr)
        #return prefix_sum
# arr=Arr([2,1,3,4,5,6,1,1,6,2,4,5,3,1])
# print(arr.reverse())
class Number:
    def __init__(self,number) -> None:
        self.num=number
    def sum_digit(self):
        my_num=self.num
        result=0
        while(my_num!=0):
                result+=my_num%10
                my_num=int(my_num/10)
        return result
arr=Arr([3, -5,-1])
print(arr.minimize_flip_k_length_subarr([1,2,3]))
