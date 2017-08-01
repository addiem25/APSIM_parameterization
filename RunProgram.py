'''
This file is what future users should run in order to 
use this program.

Created by Luke Steffen
Created on 06/14/2017
'''

from WriteTo import *

print("Please follow the prompts.")
print("NOTE: full filepath is needed if the files you wish to use\nare not in the same folder as this program")
print("EXAMPLE: C:/documents/folder/folder/exampleFile.xml")
xmlfile = input("Enter the name of the XML file: ")
csvfile = input("Enter the name of the CSV file: ")
try:
    writeTo(xmlfile, csvfile)
    print("\nCSV file data has been written to the XML file.")
except Exception as e:
    print("Something went wrong in the writing process")
    print(e)