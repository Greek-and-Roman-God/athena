# 가사 검색
# 다른풀이 https://dev-note-97.tistory.com/171

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_Value):
    right_index=bisect_right(a, right_Value)
    left_index=bisect_left(a, left_value)
    return

array=[ [] for _ in range(10001)]
reversed_array=[ [] for _ in range(10001)]

def solution(words, queries):
    answer=[]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] != '?':
            res=count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?','z'))
        else:
            res=count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.apend(res)
    return answer