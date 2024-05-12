def C_look(request_queue, head_start):
    # Sort the request queue
    request_queue.sort()
    
    # Separate into requests greater than and less than the head start
    lower_requests = [r for r in request_queue if r < head_start]
    higher_requests = [r for r in request_queue if r >= head_start]
    
    # Concatenate requests that are higher than the head, followed by requests lower than the head
    total_sequence = higher_requests + lower_requests
    
    # Start the sequence from the head position
    sequence = [head_start] + total_sequence
    
    # Calculate the total head movement
    head_movement = 0
    current_position = head_start
    
    # Calculate movement for higher requests
    for request in higher_requests:
        head_movement += abs(current_position - request)
        current_position = request
    
    # Calculate jump from highest to lowest
    if lower_requests:
        head_movement += abs(current_position - lower_requests[0])
        current_position = lower_requests[0]
    
    # Continue with lower requests
    for request in lower_requests[1:]:
        head_movement += abs(current_position - request)
        current_position = request
    
    return sequence, head_movement
