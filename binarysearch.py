'''
def Binary(arr, target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=((start+end)//2)
        if(target>arr[mid]):
            start=mid+1
        elif(target<arr[mid]):
            end=mid-1
        else:
            return mid
    return (-1)
arr=[-2,0,2,4,6,8]
target=3

print(Binary(arr,target))
'''
'''
def binary(arr, target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=((start+end)//2)
        if(target>arr[mid]):
            start=mid+1
        elif(target<arr[mid]):
            end=mid-1
        else:
            return mid
    return -1
arr=[-2,1,5,8,10]
target=9
print(binary(arr,target))
'''
'''
def binarysearch(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=((start+end)//2)
        if(target<arr[mid]):
            end=mid-1
        elif(target>arr[mid]):
            start=mid+1
        else:
            return mid
    return -1
arr=[-2,1,5,8,10]
target=8
print(binarysearch(arr,target))
'''




