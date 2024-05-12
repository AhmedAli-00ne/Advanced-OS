def C_look(request_queue, head_start):
    request_queue.sort()
    
    lower_requests = [r for r in request_queue if r < head_start]
    higher_requests = [r for r in request_queue if r >= head_start]
    
    total_sequence = higher_requests + lower_requests
    
    sequence = [head_start] + total_sequence
    
    head_movement = 0
    current_position = head_start
    
    for request in higher_requests:
        head_movement += abs(current_position - request)
        current_position = request
    
    if lower_requests:
        head_movement += abs(current_position - lower_requests[0])
        current_position = lower_requests[0]
    
    for request in lower_requests[1:]:
        head_movement += abs(current_position - request)
        current_position = request
    
    return sequence, head_movement
