def solution(num_list):

    answer = []
    last = 0
    
    # 마지막 원소 > 이전 원소 : (마지막 원소 - 이전 원소) 추가
    if num_list[-1] > num_list[-2]:
        last = num_list[-1] - num_list[-2]
    else:
        last = num_list[-1] * 2

    answer = num_list + [last]
    return answer


print(solution([2,1,6])) #=> [2,1,6,5]
print(solution([5,2,1,7,5])) #=> [5,2,1,7,5,10]  

