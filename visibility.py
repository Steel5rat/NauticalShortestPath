from shapely.geometry import LineString

def __is_correct_direction(gate_start, gate_end, from_point, to_point):
    gate_vector = (gate_end.x - gate_start.x, gate_end.y - gate_start.y)
    ray_vector = (to_point.x - from_point.x, to_point.y - from_point.y)
    cross = gate_vector[0] * ray_vector[1] - gate_vector[1] * ray_vector[0]
    return cross > 0

def is_visible_through_gates(point, gates, target_point, gate_index_start, gate_index_end):
    ray = LineString([point, target_point])
    last_distance = 0

    for i in range(gate_index_start, gate_index_end):
        left_point, right_point = gates[i]
        gate = LineString([left_point, right_point])

        if not ray.intersects(gate):
            return False

        intersection = ray.intersection(gate)

        if not __is_correct_direction(left_point, right_point, point, intersection):
            return False

        distance = point.distance(intersection)
        if distance < last_distance:
            return False
        last_distance = distance

    return True
