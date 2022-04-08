from config import settings


# class MongoDB:
#     def __init__(
#         self, connection_string: str, db_name: str, collection_name: str
#     ) -> None:
#         self.connection_string = connection_string
#         self.cluster = MongoClient(self.connection_string)
#         self.db = self.cluster[db_name]
#         self.collection = self.db[collection_name]


# class PostCollection(MongoDB):
#     def get_post(self, post_dict: dict) -> dict:
#         return self.collection.find_one(post_dict)


# CONNECTION_STRING = f"mongodb+srv://{settings.database_username}:{settings.database_password}@cluster0.slvzn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# post_collection = PostCollection(
#     connection_string=CONNECTION_STRING, db_name="instraper", collection_name="post"
# )
