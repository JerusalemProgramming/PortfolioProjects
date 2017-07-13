## IMPORT MODULES
import csv

## DEFINE FUNCTIONS
## CONNECT 2 MONGO DB
def fn_OpenFromCSV_Extract2ListOfDictionaries():

    ## OPEN CSV FILE AND EXTRACT DATA TO LIST OF PYTHON DICTIONARY OBJECTS
    
    ## CREATE EMPTY LIST TO BE USED AS LIST OF DICTIONARY OBJECTS
    ListOfDictionaries = list()
    
    ## OPENS CSV FILE AS PYTHON DICTIONARY OBJECT ~= JSON OBJECT
    with open('INPUT_MASTERINVENTORY_MERGED_NA.csv') as f:
    
        ## READ CSV DATA INTO PYTHON DICTIONARY OBJECT ~= JSON OBJECT
        f_csv = csv.DictReader(f, delimiter=';')
    
        ## SET COUNTER VARIABLE TO 0 (ZERO)
        count = 0
        
        ## BEGIN FOR-LOOP TO READ DATA FROM CSV FILE
        for row in f_csv:
    
            ## <class 'dict'> OBJECT, COUNT # OF KEY/VALUE (= ITEMS) IN EACH DICTIONARY OBJECT
            print('\n')
            print("WITHIN FUNCTION:  CSV data row MERGED MASTER INVENTORY = ",row,type(row),len(row))
    
            ## INCREMENT COUNTER FOR EACH ROW IN CSV FILE
            count = count + 1
    
            ## ADDS DICTIONARY OBJECT "ROW" AS LIST ITEM TO LIST, i.e. LIST OF DICTIONARIES
            ListOfDictionaries.append(row)
    
        print('\n')
        print("count = ",count)
    
        ## END FOR-LOOP TO READ DATA FROM CSV FILE
    
    return(ListOfDictionaries)
