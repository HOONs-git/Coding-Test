def solution(my_string, overwrite_string, s):
    answer = ''
    pre_str = my_string[:s]
    suf_str = my_string[s+len(overwrite_string):]
    answer = pre_str + overwrite_string + suf_str
    return answer