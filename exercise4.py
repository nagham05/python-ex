def check_num(nums,x):
    # print(x in nums) this prints True or False but thre funstions should return it not print so we use return 
    return x in nums

numbers = [1, 3, 5, 7, 9]
print(check_num(numbers, 3))  
print(check_num(numbers, 4)) 
