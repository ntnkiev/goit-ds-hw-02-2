from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ntnkiev:mdb162263@cluster0.hu7npum.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
db = client.ds02

try:
    db.cats.insert_one({
        "name": 'barsik',
        "age": 3,
        "features": ['ходить в капці', 'дає себе гладити', 'рудий'],
    })
    print("Successfully added")
except Exception as e:
    print(e)

try:
    db.cats.insert_many([
        {
            "name": 'Lama',
            "age": 2,
            "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            "name": 'Liza',
            "age": 4,
            "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
        },
        {
            "name": 'Boris',
            "age": 12,
            "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            "name": 'Murzik',
            "age": 1,
            "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
        },
    ])
    print("Successfully added")
except Exception as e:
    print(e)
