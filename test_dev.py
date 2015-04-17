#!/usr/bin/python
#Author: SOphie Renshaw
#Date: 10/04/2015
#Script to test the Nova Lab Exercise Solution

with open('nova_dev.py', 'r') as file1:
	with open('nova_solution.py', 'r') as file2:
		same = set(file1).intersection(file2)

same.discard('\n')

with open('compare.txt', 'w') as file_out:
	for line in same:
		file_out.write(line)

solution_count = len(open('nova_dev.py').readlines())
count = len(open('compare.txt').readlines())
i = float(count) / solution_count
marks = i*100
print marks, "%"
