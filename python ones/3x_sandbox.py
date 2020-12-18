'''
#q1
num = 122
nums = str(num)
numlis = []
faclis = []
for i in range(len(nums)):
    numlis.append(int(nums[i]))
for elem in numlis:
    if (num%elem==0):
        faclis.append(elem)
revlis = reversed(numlis)
if len(faclis)==0:
    print("No factors")
else:
    for elem in revlis:
        if elem in faclis:
            print(elem)

#q3
rows=int(input())
columns=int(input())
count_0=0

matrix=[]
for i in range(rows):
  cols=[]
  for j in range(columns):
    idx=int(input())
    if (idx == 0):
        count_0 += 1
    cols.append(idx)
  matrix.append(cols)

if (count_0>=(rows*columns)-count_0):
  print("Sparse")
else:
  print("Not sparse")

for i in range(rows):
  print(matrix[i]) 
'''  
import math
# main code
n=int(input())

# to put points in a list as [[x1,y1], [x2,y2], ...]
points_lst=[]
for e in range(n):
  x=int(input())
  y=int(input())
  points_lst.append([x, y])

# make a list of all possible distances and the list of the pairs of points
distance_lst=[] # [d1, d2, ...]
pts_d_lst=[] # [ [[x1,y1], [x1,y1]] , [[x1,y1], [x2,y2]], ... ]

for p1 in points_lst:
  for p2 in points_lst:
    if p1!=p2:
      d=math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)#formula
      distance_lst.append(d)
      pts_d_lst.append([p1, p2])

# finding all indices of munimum distance
min_d=min(distance_lst)
min_d_idx=[]
for i in range(len(distance_lst)):
  if min_d==distance_lst[i]:
    print(tuple(pts_d_lst[i][0]), tuple(pts_d_lst[i][1]))