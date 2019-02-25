#!/usr/bin/python3

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
    ]

def colWidth(tableData):
    colWidths = [0] * len(tableData)
    for col in range(len(tableData)):
        for item in tableData[col]:
            if len(item) > colWidths[col]:
                colWidths[col] = len(item)
    return colWidths

def pivot(tableData):
    columns = []
    for item in range(len(tableData[0])):
        for col in range(len(tableData)):
            try:
                columns[item].append(tableData[col][item])
            except:
                columns.append([tableData[col][item]])
    return columns

def print_table(tableData):
    length = colWidth(tableData)
    for row in pivot(tableData):
        line = ''
        for item in range(len(row)):
            line += row[item].rjust(length[item] + 1)
        print line

print_table(tableData)

#my coding
def listPrint(l):
	x = 0
	for i in l:
		string = ''
		string1 = ','.join(i)
		if string1 > string:
			string = string1
		x = len(string)
	for i in l:
		print(','.join(i).rjust(x), '*')

list1 = [['hello, this is my name'], [' I am a good man'], ['Who is this man'], ['I love China while she do not like it very much']]
listPrint(list1)
