def solution(s):
    arr = list(s)
    new_arr = sorted(arr, reverse=True)
    return ''.join(new_arr)
    
# print(solution('Zbcdefg'))
# gfedcbZ
