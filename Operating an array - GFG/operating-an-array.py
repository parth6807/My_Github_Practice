# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    if x in a: 
        return True
    else:
        return False

# fucntion must return true if 
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    a.insert(yi,y)
    return True

# fucntion must return true if 
# deletion is successful or else
# return false
def deleteEle(a, z):
    while z in a:
        a.remove(z)
    return True    
    


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        x,y,yi,z = list(map(int, input().strip().split()))
        if(searchEle(a, x)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(insertEle(a, y, yi)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(deleteEle(a, z)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        print()
# Contributed By: Harshit Sidhwa
# } Driver Code Ends