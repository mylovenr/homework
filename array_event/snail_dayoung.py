# -*- coding: utf-8 -*-
snail_array = []

for i in range(5):
	empty_array = []
	for j in range(5):
		empty_array.append(0)
	snail_array.append(empty_array)

for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print init array
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0

# change array like this
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9 

######## insert your algorithm here ########
snail_array= []
for i in range(5):
	snail_array.append([])
	for j in range(5):
		snail_array[i].append(None)


maxi=maxj=4
mini=minj=i=j=0

for c in range(1, 26):
	snail_array[i][j]= c
	
	if i==mini and j<maxj:
		j+= 1
	elif j==maxj and i<maxi:
		i+= 1
	elif i==maxi and j>minj:
		j-= 1
	elif j==minj and i>mini:
		i-= 1
	if i==maxi and j==maxj:
		mini+= 1
	elif i==maxi and j==minj:
		maxj-= 1
	elif i==mini and j==minj:
		maxi-= 1
	elif i==mini and j==maxj and mini>0:
		minj+= 1

print snail_array


for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print result array
# 영어 주석 힘들다.