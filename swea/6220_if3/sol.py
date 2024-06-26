import sys
sys.stdin = open('input.txt')       #stdin가 자동으로 입출력을 담당

T = int(input())

for tc in range(1,T+1):
    char = input()

    if char.islower():
        print(f'#{tc} {char} 는 소문자입니다.')
    else:
        print(f'#{tc} {char} 는 대문자입니다.')
