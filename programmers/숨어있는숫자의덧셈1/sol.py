def solution(my_string):
    answer = 0

    for char in my_string:
        if char in "1234567890":
            answer += int(char)
    return answer

'''
def solution(my_string):
    if char.isdigit():
        answer += int(char)
'''

'''
def solution(my_string):
    answer = 0

    for char in my_string:
        if ord('1') <= ord(char) <= ord('0') 
            answer += int(char)
    return answer
'''


print(solution("aAb1B2cC34oOp"))	#10
print(solution("1a2b3c4d123"))	#16

