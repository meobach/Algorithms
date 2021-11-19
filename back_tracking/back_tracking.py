class Back_tracking_Algorithm:
    def __init__(self) -> None:
        self.move_x=[0,1]
        self.move_y=[1,0]
    def print_permutation(self,str):
        
        print(str)
    def sum_arr(self,n):
        if(n==1):
            return 1
        return n +self.sum_arr(n-1) 
    def print_number(self,i):
        print(i)
        if(i==2):
            return
        self.print_number(i+1)
    def knight_tour(self,arr,curr):
        if(max(map(max, arr))==63):
            print(arr)
       # print(max(map(max, arr)))
        for i in range(len(self.move_x)):
            now_x=curr[0]+self.move_x[i]
            now_y=curr[1]+self.move_y[i]
            if( now_x>=0 and now_x<=7 and now_y>=0 and now_y<=7):
                value=arr[now_x][now_y]
                if(value==0):
                    arr[now_x][now_y]=arr[curr[0]][curr[1]]+1
                    self.knight_tour(arr,[now_x,now_y])
                    arr[now_x][now_y]=0
                    
                else:
                    continue
            else:
                continue
    def rat_maze(self,arr,curr):
        #print(arr)
        if(curr[0]==(len(arr[1])-1) and curr[1]==(len(arr[0])-1)):
            print(arr)
        else:
            for i in range(len(self.move_x)):
                now_x=curr[0]+self.move_x[i]
                now_y=curr[1]+self.move_y[i]
                if( now_x>=0 and now_x<=3 and now_y>=0 and now_y<=3):
                    value=arr[now_x][now_y]
                    if(value!=-1):
                        arr[now_x][now_y]=arr[curr[0]][curr[1]]+1
                        self.rat_maze(arr,[now_x,now_y])
                        arr[now_x][now_y]=0
                    else:
                        continue
                else:
                    continue
                        
            
            

arr=[]
for i in range(8):
    item=[]
    for j in range(8):
        item.append(0)
    arr.append(item)
#print(arr)
arr[0][0]=1
print(arr)
maze = [[0, 0, -1, -1],
        [0, 0, -1, 0],
        [-1, 0, -1, -1],
        [0, 0, 0, 0] ]
back_track=Back_tracking_Algorithm()
back_track.rat_maze(maze,[0,0])
# print(back_track.sum_arr(10))