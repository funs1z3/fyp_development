#!/usr/bin/python
#Author: Sophie Renshaw
#Date: 10/04/2015
#Script to test the Nova Lab Exercise Solution

with open('nova_dev.py', 'r') as file1: #opening the sample solution file
	with open('nova_solution.py', 'r') as file2: #opening student solution file
		same = set(file1).intersection(file2) #get lines that are the same

same.discard('\n') #discards blank lines

with open('compare.txt', 'w') as file_out: #opens the compare.txt file
	for line in same: #for each line that is the same in both files
		file_out.write(line) #write the line to compare.txt

solution_count = len(open('nova_dev.py').readlines()) #counts number of lines in sample solution
count = len(open('compare.txt').readlines()) #counts number of lines in the compare.txt file
i = float(count) / solution_count #divides lines in compare by lines in solution 
marks = i*100 #gets percentage
print marks, "%" #returns to user
