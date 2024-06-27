def solution(n, k):
    answer = 0

    for i in range(n):
        if n//10 < 1:
            answer = n*12000 + k*2000
        else:
            answer = n*12000 + k*2000 - (n//10)*2000
    return answer

print(solution(10,3))
print(solution(64,6))