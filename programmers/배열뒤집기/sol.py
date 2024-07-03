def solution(num_list):
    answer = []
    temp = 0
    last = len(num_list)

    for i in range(last):
        num_list[i]   
        num_list[last -1] = num_list[i]
        num_list[i] = temp

        answer.append(i)
    return answer

print(solution([1, 2, 3, 4, 5])) #5,4,3,2,1
print(solution([1,1,4,5,7,4,2]))