'''
def solution(my_string, overwrite_string, s):
    answer = my_string
    for i in range(len(overwrite_string)) :
        answer[s+i] = my_string[i]
    
    return answer
'''
def solution(my_string, overwrite_string, s):
    # 1. 접두사 (Prefix): s 인덱스 앞부분까지 자릅니다.
    prefix = my_string[:s]
    
    # 2. 덮어쓰기가 끝나는 인덱스를 계산합니다.
    overwrite_end_index = s + len(overwrite_string)
    
    # 3. 접미사 (Suffix): 덮어쓰기가 끝난 지점부터 문자열의 끝까지 자릅니다.
    suffix = my_string[overwrite_end_index:]
    
    # 4. 세 부분을 연결하여 새로운 문자열을 만듭니다.
    answer = prefix + overwrite_string + suffix
    
    return answer