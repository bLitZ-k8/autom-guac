import math


def distance(x1, y1, x2, y2):
    # defining function for finding distance that takes 2 pairs of coordinates
    # while calling the function, we will pass tuples to get unpacked
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist


n = int(input())
points_lst = []  # list for containing tuples of points
dist_lst = []  # list for containing distances
pt_pairs = []  # list for containing pairs of points, no duplicacy

for i in range(n):
    x = int(input())
    y = int(input())
    points_lst.append((x, y))

for ind1 in range(len(points_lst)):
    for ind2 in range(ind1+1, len(points_lst)):
        # n can be used here too, personal choice maybe
        # to make sure no duplicate pairs of points are appended, you can make sure that the 2 points are of adjacent positions in base case
        # duplicacy happens when for example 3rd point will pair with 1st and 2nd, so start the inner loop with the next index: 4th
        p1 = points_lst[ind1]
        p2 = points_lst[ind2]
        if p1 != p2:
            # * operator unpacks tuple contents and passes then in the order they are unpacked
            d = distance(*p1, *p2)
            dist_lst.append(d)
            pt_pairs.append([p1, p2])
min_d = min(dist_lst)
min_d_idx = [i for i, e in enumerate(dist_lst) if e == min_d]
# used list comprehension to find index of all instances of min distance in dist_list
# i,e is the syntax that the iterating function enumerate uses

for f in min_d_idx:
    print(pt_pairs[f][0], pt_pairs[f][1])
