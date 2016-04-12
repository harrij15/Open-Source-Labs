from pymongo import MongoClient
import random
import datetime
client = MongoClient()
db = client.test_database
#collection = db.definitions
size = 0

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    index = random.randrange(0,size)

    i = 0

    d = dict()

    for post in db.definitions.find():
	if i == index:
	    d = post
            print d
	    word = d["word"]
	    definition = d["definition"]
	    dateArray = d["date"]
            break
	i += 1
 
    dateArray.append(datetime.datetime.utcnow())
    db.definitions.update({"word": word}, {"$push": { "date" : dateArray } } )

    return "%s: %s" %(word,definition)

if __name__ == '__main__':

    #print db.posts.find()
	
    posts = db.definitions

    """db.definitions.insert_one({"word": "hobnob", "definition": "to associate familiarly"})
    db.definitions.insert_one({"word": "invincible", "definition": "incapable of being conquered, overcome, or subdued"})
    db.definitions.insert_one({"word": "compare", "definition": "to say that (something) is similar to something else"})
    db.definitions.insert_one({"word": "wherefore", "definition": "for what reason or purpose"})
    db.definitions.insert_one({"word": "exasperate", "definition": "the excite the anger of"})"""
    
    for post in db.definitions.find():
	size += 1

	#print post


    #print size

	

    print random_word_requester()

    for post in db.definitions.find():
        print post
