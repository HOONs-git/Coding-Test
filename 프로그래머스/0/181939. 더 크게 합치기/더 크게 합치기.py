def solution(a, b):
    answer = 0
    '''
    a_b = (string)a + (string)b
    b_a = (string)b + (string)a
    '''
    a_b = str(a) + str(b)
    b_a = str(b) + str(a)
    if int(a_b) > int(b_a) :
        return int(a_b)
    else :
        return int(b_a)
    #return answer