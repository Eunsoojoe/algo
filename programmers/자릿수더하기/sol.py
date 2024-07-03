def solution(n):
    answer = 0
    n = str(n)
    for char in n:
        answer += int(char)
    return answer


print(solution(1234)) #10
print(solution(930211)) #16