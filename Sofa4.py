import pandas as pd
import json

with open('points.json', 'r') as f:
    points_data = json.load(f)

points_series = pd.Series(points_data)

distances = points_series.diff().dropna().abs()

distances_dict = distances.to_dict()
with open('len.json', 'w') as f:
    json.dump(distances_dict, f)


