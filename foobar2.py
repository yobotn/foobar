def solution(s):
    result = 0
    for index, direction in enumerate(list(s)):
        if (direction == '>'):
            result += s[index:].count('<')
    return result*2

print(solution('>----<'))
print(solution('<<>><'))
print(solution('--->-><-><-->-'))