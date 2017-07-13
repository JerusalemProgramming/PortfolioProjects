## IMPORT MODULES
import sys
import pymongo

## DEFINE FUNCTIONS
## CONNECT 2 MONGO DB SERVER
def fn_Connect2MongoDBServer():
    """ Connect to MongoDB """
    
#try:
    ## TRY TO CREATE MONGO CLIENT
    MongoDBClient = pymongo.MongoClient('mongodb://localhost:27017/')
    
    ## TEST OUTPUT
    print("\n")
    print("WITHIN FUNCTION:  Connected successfully to MongoDBClient on LOCALHOST:PORT27017")
    print("WITHIN FUNCTION:  MongoDBClient = ", MongoDBClient)
    
    
#except pymongo.errors.ConnectionFailure as e:
#    ## RAISE EXCEPTION / ERROR
#    
#    ## TEST OUTPUT
#    print("\n")
#    print("WITHIN FUNCTION:  WTF - Something went wrong - Connection Failure!!")
#    sys.stderr.write("WITHIN FUNCTION:  Could not connect to MongoDB: %s" % e)
#    sys.exit(1)
    
    return(MongoDBClient)
