## IMPORT MODULES

## DEFINE FUNCTIONS
## GET ALL DATA FROM DB        
def fn_GetAllDataFromDB(db):
    
#try:
    ## GET DATA FROM DB
    
    DataRetrievedFromDB = db.inventory.find({}).limit(0) ## 0 SETS LIMIT TO NO LIMIT; 1 sets limit to 1 item i.e. ABOVE 20 ITEM CURSOR DEFAULT LIMIT
  
    ## TEST OUTPUT
    print("\n")
    print("WITHIN FUNCTION:  Successfully RETRIEVED document: %s" % DataRetrievedFromDB)
    
    print("\n")
    print("WITHIN FUNCTION:  type(DataRetrievedFromDB) = ", type(DataRetrievedFromDB))
    
    return(DataRetrievedFromDB)
    
    
#except:
#    ## EXCEPTION / ERROR
#    ## TEST OUTPUT
#    print("\n")
#    print("WTF - Something went wrong - Could not insert item(s) to DB!")