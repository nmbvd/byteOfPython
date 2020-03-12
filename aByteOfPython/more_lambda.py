def qu_y(dict):
    return dict['y']

points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
#points.sort(key=qu_y)
print(points)

