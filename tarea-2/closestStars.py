import sys
import math

def read_input():
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    index = 0
    cases = []
    while index < len(data):
        n = data[index]
        index += 1
        points = []
        for _ in range(n):
            x = data[index]
            y = data[index + 1]
            points.append((x, y))
            index += 2
        cases.append(points)
    return cases

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    if len(points_sorted_by_x) <= 3:
        return brute_force_closest_pair(points_sorted_by_x)
    
    mid = len(points_sorted_by_x) // 2
    left_points = points_sorted_by_x[:mid]
    right_points = points_sorted_by_x[mid:]
    
    midpoint_x = points_sorted_by_x[mid][0]
    
    left_y_sorted = [point for point in points_sorted_by_y if point[0] <= midpoint_x]
    right_y_sorted = [point for point in points_sorted_by_y if point[0] > midpoint_x]
    
    (d_left, pair_left) = closest_pair_recursive(left_points, left_y_sorted)
    (d_right, pair_right) = closest_pair_recursive(right_points, right_y_sorted)
    
    d_min = min(d_left, d_right)
    if d_left < d_right:
        min_pair = pair_left
    else:
        min_pair = pair_right
    
    (d_split, pair_split) = closest_split_pair(points_sorted_by_x, points_sorted_by_y, d_min)
    
    if d_split < d_min:
        return (d_split, pair_split)
    else:
        return (d_min, min_pair)

def brute_force_closest_pair(points):
    min_distance = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                pair = (points[i], points[j])
    return (min_distance, pair)

def closest_split_pair(points_sorted_by_x, points_sorted_by_y, delta):
    mid_x = points_sorted_by_x[len(points_sorted_by_x) // 2][0]
    in_strip = [p for p in points_sorted_by_y if mid_x - delta <= p[0] <= mid_x + delta]
    
    min_distance = delta
    pair = None
    for i in range(len(in_strip)):
        for j in range(i + 1, min(i + 7, len(in_strip))):
            p, q = in_strip[i], in_strip[j]
            distance = euclidean_distance(p, q)
            if distance < min_distance:
                min_distance = distance
                pair = (p, q)
    return (min_distance, pair)

def closest_pair(points):
    points_sorted_by_x = sorted(points)
    points_sorted_by_y = sorted(points, key=lambda point: point[1])
    (min_distance, _) = closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)
    return min_distance

def main():
    cases = read_input()
    for points in cases:
        min_distance = closest_pair(points)
        print(f"{min_distance:.6f}")

if __name__ == "__main__":
    main()
