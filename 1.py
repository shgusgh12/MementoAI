def solution(arr):
    min_num = min(arr)
    
    new_arr = [num for num in arr if num != min_num]
    
    if len(new_arr) == 0:
        return [-1]
    else:
        return new_arr
    
# print(solution([4,3,2,1])) 
# [4,3,2]

# print(solution([10]))
# [-1]
