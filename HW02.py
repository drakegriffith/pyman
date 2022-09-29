##########################################
# All Necessary Modules Have Been Imported
# Do Not Import Any Additional Modules
##########################################

import json, datetime, csv
from pprint import pprint

## NOTES:

# CS 2316 - Fall 2022 - HW02 CSV Module, Data Exchange Formats
# HW02: This homework is due by Wednesday, September 14th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...

# This homework is divided into two sections.
# Questions 1-3 require you to download the "NovelEnglish_All.txt" file
# Questions 4-5 require you to download the "sku.csv" and "WarehouseLocations.csv" files

# The questions within each section require the outputs of the previous questions
# so they must be completed in order and the previous output needs to be correct in order to proceed

# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW02.py  - Your submission should be named exactly HW02.py

def txt_to_csv(input_file):
	with open(input_file, 'r') as fin:
		reader = csv.reader(fin, delimiter='\t')
		readerList = [list(line[0:4]) for line in reader]
	fin.close()
	with open('novels.csv', 'w') as fin:
		writer = csv.writer(fin, delimiter=',')
		for listElement in readerList:
			writer.writerow(listElement)
	
	return readerList
	
	"""
	Question 1
	- NovelEnglish_All.txt contains information about English novels.
	- Read the NovelEnglish_All.txt with FILE I/O or CSV.
	- Use a list of lists to create a CSV file with the appropriate data WITHOUT WHITESPACE (remove \n) named "novels.csv".
	- Ensure you using the correct delimiter for each line ("\t")
	- Exclude the "Corpus" column, and strip the quotes from the "Author" column.
	- Return the list of lists.

	Args:
		input_file (NovelEnglish_All.txt)
	Returns:
		List of lists

	Output:
	[['id', 'Year', 'Author', 'Title'],
	['1', '2001', 'Martel,Yann', 'LifeofPi'],
	['2', '2002', 'Kidd,SueMonk', 'TheSecretLifeofBees'],
	['3', '2002', 'Sebold,Alice', 'LovelyBones'],
	['4', '2003', 'Hosseini,Khaled', 'TheKiteRunner'],
	...
	['1210', '2015', 'William,EliKP', 'CashCrashJubilee'],
	['1211', '2015', 'Womack,Gwendolyn', 'TheMemoryPainter']]
	"""

def write_to_json(input_file, output_file):
	outerDict = { }
	
	with open(input_file, 'r') as fin:
		reader = csv.reader(fin)
		readerList = [list(line[0:4]) for line in reader if len(line) != 0]
	fin.close()
	
	for item in readerList:
		print(item[1])
		if (item[1]) not in outerDict:
			nestedDict = { 'Authors': 1, 'Titles': 1 }
			outerDict[item[1]] = nestedDict
			print('created')
		else:
			outerDict[item[1]]['Authors'] += 1
			outerDict[item[1]]['Titles'] += 1
		continue

	output_file = json.dumps(outerDict, indent=4)
	return outerDict


	"""
	Question 2
	- Using the csv file from question 1, create a
	dictionary mapping years to an inner dictionary.
	- The inner dictionary keys should be "Authors", "Titles" with
	the number of authors and titles in that year as their value.
	- Write the dictionary to a JSON file with the name passed in as output_file.
	- Return the dictionary.

	Args:
		input_file (novels.csv)
		output_file (str)
	Returns:
		Nested dictionary
`

	Output:
	{'2001': {'Authors': 2,
			'Titles': 2},
	'2002': {'Authors': 4,
			'Titles': 4},
	'2003': {'Authors': 3,
			'Titles': 3},
	'2004': {'Authors': 2,
			'Titles': 2},
	...
	'2015': {'Authors': 239,
			'Titles': 239}}

	"""

	pass

def author_history(cleaned_list):
	openDict = {}
	readerList = [list(line) for line in cleaned_list]
	for item in readerList :
	
		if item[2][0] == "S":
			insideDict = { 'First Book' : item[3] , 'Last Book' : item[3], 'Number of Books' : 1}
			openDict[item[2]] = insideDict
			print(item[2])
	return openDict

	"""
	Question 3
	- Using the cleaned list of lists from question 1, create a dictionary of dictionaries
	  where each key in the outer dictionary is an author whose last name starts with the letter 'S'.
	- Each inner dictionary should contain the number of books that author has written as 'Number of Books'
	- It should contain the earliest book title for that author based on year with the key 'First Book'
	- Finally it should contain the latest book title for that author based on year with the key 'Last Book'
	- If an author has only one book put the same title in both places
	- Return the dictionary of dictionaries

	Args:
		cleaned_list (list)
	Returns:
		dictionary of dictionaries

	Output:
		{'SafranFoer,Jonathan': {'First Book': 'ExtremelyLoudandIncrediblyClose',
                         		 'Last Book': 'ExtremelyLoudandIncrediblyClose',
                         		 'Number of Books': 1},
 		 'Salter,James': {'First Book': 'LastNight',
                  		  'Last Book': 'LastNight',
                  		  'Number of Books': 1},
             ...
         'Szado,Ania': {'First Book': 'StudioSaintEx',
                		'Last Book': 'StudioSaintEx',
                		'Number of Books': 1}}
	"""

	pass

#############################################################
#Question 4, 5, and 6 use sku.csv and WarehouseLocations.csv#
#############################################################

def warehouse_stats(sku):
	newSKUStats = {}
	with open (sku, 'r') as fin:
		reader = csv.reader(fin, dialect='excel')
		head = next(reader)
		readerList = [list(line) for line in reader]
	
	fin.close()
	totalWarehouse = 0
	totalValid = 0 
	for stat in readerList:
		if stat[1] != "N/A":
			warehouseNum = int(stat[3]) if int(stat[2]) >= 0 else 0
			totalWarehouse += warehouseNum
			totalValid += 1
			innerDict = { '350 Loc ': True if stat[2] !=0 else False, 'Warehouse Qty': stat[3], 'Forcasted Qty' : stat[4], 'Items/Day': round((float(stat[6]))/(float(stat[5])),5) if (float(stat[6]) and float(stat[5])) > 0 else round((float(stat[4])*.1 / 5.0), 5) }
			newSKUStats[stat[1]] = innerDict
	newSKUStats['Totals'] = { 'Qty' : totalWarehouse, 'Valid' : totalValid}
	return newSKUStats
	"""
	Question 4
	- Read sku.csv with CSV and create a dictionary of the New SKU Statistics.
	- The New Sku should be the key, with the corresponding value being an inner
			dictionary containing the following statistics:
				- 350 Loc: True if not 0
				- Warehouse Qty
				- Forcasted Qty
				- Items/Day: can be calculated using CuFt/Day divided by Item Cube.
							This result should be an float rounded to 5 decimals places.

	- In your warehouse dictionary, add an inner dictionary with key Totals which contains:
			- Total Qty in Warehouse as key "Qty": Do Not add to Totals if '350 Loc' is not a valid location.
			- Number of Valid 350 Loc as key "Valid"

	Data Cleaning Steps:
	- In some variates of New Sku #, the Item Cube & CuFt/Day are faulty.
			Fix the manufacturers mistake. If either is **less than or equal to 0**,
			Item Cube can be assumed to be 5.0 and CuFt/Day is 10% of the
			Forcasted Qty of the New Sku #. Calculate similarly, with Forcasted Qty divided
			by Item Cube, and round to 5 decimal places.

	- Ensure the New SKU number is valid. Do not add to your new dictionary or calucalte in totals
			of the New SKU number of "#N/A"

	Assumptions:
	- You can assume all New Sku numbers are unique.
	- Do not assume values are integers even if they appear to be numbers. You may have to cast to integers or floats.

	Return your final warehouse_stats dictionary

	Args:
		sku (csv file)
	Return:
		dict

	Last five elements displayed:
	>> warehouse_stats('sku.csv')

	.....
 '63149901': {'350 Loc': True,
              'Forecasted Qty': '1315',
              'Items/Day': 26.3,
              'Warehouse Qty': '2304'},
 '63149902': {'350 Loc': True,
              'Forecasted Qty': '1458',
              'Items/Day': 29.16,
              'Warehouse Qty': '3072'},
 '63149904': {'350 Loc': True,
              'Forecasted Qty': '1324',
              'Items/Day': 26.48,
              'Warehouse Qty': '1536'},
 '63149905': {'350 Loc': True,
              'Forecasted Qty': '413',
              'Items/Day': 8.26,
              'Warehouse Qty': '1920'},
 'Totals': {'Qty': 3861258, 'Valid': 3327}}

	"""

	pass

def update_warehouse(stats,input_file):
	outerDict = {}
	print(stats)
	with open(input_file, 'r') as fin:
		reader = csv.reader(fin)
		head = next(reader)
		readerList = [list(line) for line in reader]
	quantityCount = 0
	validCount = 0
	for item in readerList:
		if item[0] != "#N/A":
			quantityCount += int(stats[item[0]]['Warehouse Qty'])
			validCount += 1
			innerDict = { 'Forecasted Quantity' : stats[item[0]]['Forcasted Qty'], 'Items/Day' : stats[item[0]]['Items/Day'], 'New Location': item[1], 'Warehouse Qty' : stats[item[0]]['Warehouse Qty']}
			outerDict[item[0]] = innerDict
	outerDict['Totals'] = { 'Qty' : quantityCount , 'Valid': validCount}
	return outerDict
	'''
	Question 5
	- The warehouse layout was recently optimized to be organized in specific warehouse locations.
	- Given an input_file 'Warehouse_Locations.csv' containing the New Sku numbers with their
			associated location and your outputted dictionary 'stats' from Question 4,
			match each New Sku number and replace '350 Loc' in your stats dictionary
			with 'New Location' mapped to Warehouse Location from 'Warehouse_Locations.csv'

	- Similar to 'sku.csv', some New Sku numbers are invalid. Skip over the invalid sku numbers,
			i.e. '#N/A'

	Args:
		dictionary (stats)
		input_file (csv file)
	Return:
		dictionary
	Output:
	Last five elements displayed:
	>> update_warehouse(warehouse_stats(sku), 'WarehouseLocations.csv')

	...

		 '63149901': {'Forecasted Qty': '1315',
		              'Items/Day': 26.3,
		              'New Location': 'D14',
		              'Warehouse Qty': '2304'},
		 '63149902': {'Forecasted Qty': '1458',
		              'Items/Day': 29.16,
		              'New Location': 'A6',
		              'Warehouse Qty': '3072'},
		 '63149904': {'Forecasted Qty': '1324',
		              'Items/Day': 26.48,
		              'New Location': 'B14',
		              'Warehouse Qty': '1536'},
		 '63149905': {'Forecasted Qty': '413',
		              'Items/Day': 8.26,
		              'New Location': 'A8',
		              'Warehouse Qty': '1920'},
		 'Totals': {'Qty': 3861258, 'Valid': 3327}}
	'''

	pass


if __name__ == '__main__':
	# Question 01:
	#pprint(txt_to_csv("NovelEnglish_All.txt"))

	# Question 02:
	#pprint(write_to_json("novels.csv", "novels_output.json"))

	# Question 03:
	#pprint(author_history(txt_to_csv("NovelEnglish_All.txt")))

	# Question 04:
	#pprint(warehouse_stats('sku.csv'))

	# Question 05:
	stats = warehouse_stats('sku.csv')
	pprint(update_warehouse(stats, "WarehouseLocations.csv"))

	#
