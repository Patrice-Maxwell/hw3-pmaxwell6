# 1. Play the FizzBuzz Game w/ 1-100 incluv.
# Helper links <
# https://www.w3schools.com/python/ref_func_range.asp
# https://realpython.com/python-modulo-operator/
# >

# Unexpected Errors
#   <   nums = range(6,11)
#       for x in nums:
#          print(nums[x])
#   > This gave me an OOB error and Im not sure why?

x = range(1,101)
for num in x:
    if x[num-1] % 15 == 0:
        print("WhizBang") 
    
    elif x[num-1] % 5 == 0:
        print("Bang")

    elif x[num-1] % 3 == 0:
        print("Whiz")

    else:
     print( x[num])

print("Like 3 seconds")


# 2. Sphere Volume 
# Helper links <
# https://www.w3schools.com/python/module_math.asp
# 
# >
import math

def volume(r):
    print("The radius, ", r , )
    v = math.pi * 4/3 * math.pow(r, 3)
    print("will produce a sphere with the volume " ,v )

volume(5)


# 3. CVS
# Helper links <
# https://www.w3schools.com/python/python_dictionaries_nested.asp
# https://www.pythontutorial.net/python-basics/python-write-csv-file/
# https://stackoverflow.com/questions/334655/passing-a-dictionary-to-a-function-as-keyword-parameters
# >

import csv
import sys
import itertools


libheaders = ["Title" , "author", "ISBN13" , "pages"] 

mylib = {
    "1984" : {
        "author": "George Orwell",
        "ISBN13": "978-0451524935",
        "pages" : "268"
    },
    "Harry Potter and the Sorcerer's Stone" : {
        "author": "J.K Rowling",
        "ISBN13": "978-0590353403",
        "pages" : "223"
    },
    "The Stinky Cheese Man and Other Fairly Stupid Tales" : {
        "author": "J.K Rowling",
        "ISBN13": "978-0670844876",
        "pages" : "56"
    },
    "The Angel's Kiss: A Melody Malone Mystery" : {
        "author": "Melody Pond",
        "ISBN13": "978-1448141333",
        "pages" : "80"
    }
}

def csvmkir(headers , output_file_name , **dictionary):
    with open('C:/Users/patri/Downloads/' + output_file_name , 'w' , encoding='UTF8' ) as f:
        writer = csv.DictWriter(f , headers)
        for key,val in dictionary.items():
            row = {'Title' : key}
            row.update(val)
            writer.writerow(row)
    return output_file_name
    
csvmkir(libheaders , 'lib2.csv', **mylib )


# 4. CVS Print Reverse
# Helper links <
# https://medium.com/swlh/how-to-parse-a-csv-to-create-a-nested-dictionary-python-61d5a6934eb9
#
# >

with open('C:/Users/patri/Downloads/lib2.csv' , 'r') as f:
    file_read = csv.reader(f)
    for lines in file_read:
        print(lines)

# 5. CVS Tempfile
# Helper links <
# 
#
# >