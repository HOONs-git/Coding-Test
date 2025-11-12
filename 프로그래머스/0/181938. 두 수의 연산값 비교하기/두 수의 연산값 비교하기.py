def solution(a, b):
    answer = 0
    a_b = str(a) + str(b)
    ab2 = 2*a*b
    if int(a_b) >= ab2 :
        return int(a_b)
    else :
        return ab2
    #return answer