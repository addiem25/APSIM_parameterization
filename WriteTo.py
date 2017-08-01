'''
This is a function that writes to a XML from a CSV file.
This program is specifically used for writing data on 
sorghum from a CSV file to a XML file in a quick and 
streamline fashion.

Created by Luke Steffen
Created on 06/13/2017
'''

import xml.etree.ElementTree as xml
import csv as csv
import sys

def writeTo(xml_file, csv_file):
    '''This function takes a XML and CSV file and reads data from the CSV file and
    writes it into the XML file.
    @param: XML and CSV file
    Return: void
    Luke Steffen''' 
    #This try block open the files safely
    try:
        csvfile = open(str(csv_file), "r")
    except FileNotFoundError as e:
        print(e)
        sys.exit(-1)
    #This block before the loop begins a parse on the XML file and stores the CSV data in a list of dictionaries
    dictionary = csv.DictReader(csvfile)
    tree = xml.parse(xml_file)
    root = tree.getroot()
    #This for loop retrieves the correct subroot and assigns it a variable name
    for child in root:
        if (child.tag == "Model"):
            subroot = child
    '''This for loop goes through the list of dictionaries, finding the cultivar/subroot name.
    Once it has found the subroot, the for loop places all other dictionary fieldnames under the 
    subroot as subelements. The loop finishes by appending the subroot to the main root.'''
    for row in dictionary:
        subelem1 = xml.SubElement(subroot, row['cultivar'], cultivar="yes")
        for name in dictionary.fieldnames:
            if (name != "cultivar"):
                if (name == "tt_endjuv_to_init"):
                    subelem = xml.SubElement(subelem1, name, units="OC", description="fixed for all genotypes")
                    subelem.text = row[name]
                else:
                    subelem = xml.SubElement(subelem1, name)
                    subelem.text = row[name]
     
    tree.write(xml_file)
    csvfile.close()


    
    
    