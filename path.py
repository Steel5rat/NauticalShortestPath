import heapq

from visibility import is_visible_through_gates

def find_shortest_path(gates, start_point, end_point):
    # to get rid of corner case, will consider end_point as a yet another gate 
    gates.append((end_point, end_point))

    visited = set()
    heap = []
    heapq.heappush(heap, (0, start_point, [start_point], 0))

    while heap:
        distance, point, path_so_far, next_gate_index = heapq.heappop(heap)
        if point in visited:
            continue
        if point == end_point:
            return path_so_far
        
        visited.add(point)

        for visible_point, gate_offset in __get_visible_points(gates, point, next_gate_index):
            if visible_point in visited:
                continue
            distance_increase = point.distance(visible_point)
            heapq.heappush(heap, (distance + distance_increase, visible_point, list(path_so_far) + [visible_point], next_gate_index + gate_offset))
    
    raise Exception('Path not found')

def __get_visible_points(gates, point, next_gate_index):
    visible_points = []
    for i in range(next_gate_index, len(gates)):
        gate_offset = i - next_gate_index + 1
        left, right = gates[i]
        left_visible = is_visible_through_gates(point, gates, left, next_gate_index, i)
        right_visible = is_visible_through_gates(point, gates, right, next_gate_index, i)
        
        if not left_visible and not right_visible:
            return visible_points

        if left_visible:
            visible_points.append((left, gate_offset))
        if right_visible:
            visible_points.append((right, gate_offset))

    return visible_points