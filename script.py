# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:04:13 2020

@author: sreet
"""

# import csv

# inputfile = csv.reader(open('nha_indicators.csv','r'))


# for row in inputfile:
#     print(row)


# import pandas as pd
 	
# csv_file = pd.DataFrame(pd.read_csv("nha_indicators.csv", sep = ",",
#     names = ["Countries", "Indicators","2000","2008","2018"], 
#     header=1))
# csv_file.to_json("nha_indicators.json")


# import csv 
# import json 


# # Function to convert a CSV to JSON 
# # Takes the file paths as arguments 
# def make_json(csvFilePath, jsonFilePath): 
 	
#  	# create a dictionary 
#       data = {} 
 	
#  	# Open a csv reader called DictReader 
#       with open(csvFilePath) as csvf: 
#           Reader = csv.DictReader(csvf) 
# 		
# 		# Convert each row into a dictionary 
# 		# and add it to data 
#           for rows in Reader: 
 			
#  			# Assuming a column named 'Index' to 
#  			# be the primary key 
#               key = rows['Index'] 
#               data[key] = rows 

#  	# Open a json writer, and use the json.dumps() 
#  	# function to dump data 
#       with open(jsonFilePath, 'w') as jsonf: 
#           jsonf.write(json.dumps(data, indent=4)) 
# 		
# # Driver Code 

# # Decide the two file paths according to your 
# # computer system 
# csvFilePath = r'nha_indicators.csv'
# jsonFilePath = r'nha_indicators.json'

# # Call the make_json function 
# make_json(csvFilePath, jsonFilePath)


import csv
import json

csvfile = open('nha_indicators.csv', 'r')
jsonfile = open('nha_indicators.json', 'w')

fieldnames = ("Index","Countries","Indicators",2000,2001,2002,2003,2004,2005,2006,2007,
              2008, 2009, 2010,2011,2012,2013,2014,2015,2016,2017,2018)
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
