import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist
n = int(input())
points_lst = []
dist_lst = []
pt_pairs = []

for i in range(n):
    x = int(input())
    y = int(input())
    points_lst.append((x, y))

for p1 in points_lst:
    for p2 in points_lst:
        if p1!=p2:
            d = distance(*p1, *p2)
            dist_lst.append(d)
            pt_pairs.append([p1, p2])
min_d = min(dist_lst)
min_d_idx = [i for i,e in enumerate(dist_lst) if e==min_d]

for i in min_d_idx:
    print(pt_pairs[i][0], pt_pairs[i][1])
