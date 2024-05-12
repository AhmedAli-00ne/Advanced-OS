def FCFS(req_queue_list, head_start_value):
    path = [head_start_value]
    totalMovement = 0
    for i in range(len(req_queue_list)):
        path.append(req_queue_list[i])
        totalMovement += abs(req_queue_list[i] - path[-2])
    return path, totalMovement
