import csv
import json
 
# This code is improved version of CSV to JSON file convertor. Solves the problem of using first column name as Primary Key
# Added -sig in UTF8 encoding while reading csv file to resolve the problem of reading first column name. If not specified first column in appended with \ufeff

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader.
    # Added -sig in encoding to resolve the problem of reading first column name. Removing ByteOrderMark from first colum of each row
    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'handleId' to
            # be the primary key
            print(rows)
            key = rows['handleId']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
#csvFilePath = r'catalog_products.csv'
#jsonFilePath = r'Names.json'
csvFilePath = r"catalog_products.csv"
jsonFilePath = r"Product.json"
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)
