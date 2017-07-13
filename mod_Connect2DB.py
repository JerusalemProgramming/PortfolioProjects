## DEFINE FUNCTIONS
## CONNECT 2 DB        
def fn_Connect2DB(MongoDBClient):
    
    try:
        ## DEFINE DATABASE TO WHICH TO CONNECT
        db = MongoDBClient.customdb
        
        ## TEST OUTPUT
        print("\n")
        print("WITHIN FUNCTION:  Okie Dokie - RWA!")
        print("WITHIN FUNCTION:  db.name = ", db.name)
        print("WITHIN FUNCTION:  db = ", db)
        print("WITHIN FUNCTION:  db.collections = ", db.collections)
        print("WITHIN FUNCTION:  type(db) = ", type(db))
        
    except:
        ## EXCEPTION / ERROR
        ## TEST OUTPUT
        print("\n")
        print("WITHIN FUNCTION:  WTF - Something went wrong - Could not connect to DB!")
    
    
    return(db)
