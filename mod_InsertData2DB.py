## IMPORT MODULES

## DEFINE FUNCTIONS
## INSERT DATA 2 DB        
def fn_InsertData2DB(db, Data2Insert2DB):
    
#try:
    ## INSERT DATA INTO DB
    
    ## INSERTS ONE DICTIONARY OBJECT INTO DB.collection; CREATES DB COLLECTION "inventory"
    #db.inventory.insert_one(Data2Insert2DB)
    
    ## INSERTS LIST OF DICTIONARY OBJECTS TO DB.collection; CREATES DB COLLECTION "inventory"
    db.inventory.insert_many(Data2Insert2DB)
    
    ## TEST OUTPUT
    print("\n")
    print("WITHIN FUNCTION:  Successfully INSERTED document: %s" % Data2Insert2DB)
    print("\n")
    print("WITHIN FUNCTION:  type(Data2Insert2DB) = ", type(Data2Insert2DB))
    
    return(Data2Insert2DB)
    
    
#except:
#    ## EXCEPTION / ERROR
#    ## TEST OUTPUT
#    print("\n")
#    print("WTF - Something went wrong - Could not insert item(s) to DB!")
