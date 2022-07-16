def solution(array, commands):
    answer = []
    for command in commands:
        c_array = array[command[0]-1:command[1]]
        c_array.sort()
        answer.append(c_array[command[2]-1])
    return answer
