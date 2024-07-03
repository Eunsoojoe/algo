'''
def solution(my_string, letter):
    answer = ''
    answer = my_string.replace(letter,'')

    return answer
'''

def solution(my_string, letter):
    answer = ''
    for char in my_string:
        # 지우려는 대상과 같지 않을 때
        if char != letter:
            answer += char    # 문자를 더하면 concac 한다는 뜻
        
    return answer
            


print(solution("abcdef","f")) #abcde
print(solution("BCBdbe","B")) #Cdbe

