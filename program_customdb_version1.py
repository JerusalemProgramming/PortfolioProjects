## IMPORT MODULES
import mod_OpenFromCSV_Extract2ListOfDictionaries
import mod_Connect2MongoDBServer
import mod_Connect2DB
import mod_InsertData2DB
import mod_GetAllDataFromDB

## DECLARE VARIABLES 
## DATA OF VARIABLES TO BE EXTRACTED FROM CSV FILE (BELOW)

## BEGIN MAIN PROGRAM        
if __name__ == "__main__":
    
    ## CALL MODULE.FUNCTION - fn_OpenFromCSV_Extract2ListOfDictionaries(); OPEN CSV DATA FILE
    ListOfDictionariesFromCSV = mod_OpenFromCSV_Extract2ListOfDictionaries.fn_OpenFromCSV_Extract2ListOfDictionaries()
    print("\n")
    print("WITHIN PROGRAM:  type(ListOfDictionariesFromCSV) = ", type(ListOfDictionariesFromCSV))
    
    ## DECLARE VARIABLES
    ## DATA OF VARIABLES TO INSERT TO DB
    Data2Insert2DB = ListOfDictionariesFromCSV
    
    ## CALL MODULE.FUNCTION - fn_Connect2MongoDBServer(); CONNECT TO MONGO DB SERVER WITH CLIENT VARIABLE
    MongoDBClient = mod_Connect2MongoDBServer.fn_Connect2MongoDBServer()
    print("\n")
    print("WITHIN PROGRAM:  type(MongoDBClient) = ", type(MongoDBClient))
    
    ## CALL MODULE.FUNCTION - fn_Connect2DB(); pass 1 parameter:  1.) MongoDBClient; CONNECT TO MONGO DB CLIENT WITH DB VARIABLE
    db = mod_Connect2DB.fn_Connect2DB(MongoDBClient)
    print("\n")
    print("WITHIN PROGRAM:  type(db) = ", type(db))
    
    ## CALL MODULE.FUNCTION - fn_InsertData2DB(); pass 2 parameters:  1.) db; 2.) Data2Insert2DB - DOES NOT DELETE DB TO START WITH EMPTY MONGO DB!!!
    DataInserted2DB = mod_InsertData2DB.fn_InsertData2DB(db, Data2Insert2DB)
    print("\n")
    print("WITHIN PROGRAM:  type(DataInserted2DB) = ", type(DataInserted2DB))
   
    ## CALL MODULE.FUNCTION - fn_GetAllDataFromDB(); pass 1 parameter:  1.) db
    GetAllDataFromDB = mod_GetAllDataFromDB.fn_GetAllDataFromDB(db)
    print("\n")
    print("WITHIN PROGRAM:  type(GetAllDataFromDB) = ", type(GetAllDataFromDB))
    
    
    
    
    
    
