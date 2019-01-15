from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class Dao:
	def __init__(self):
		connection = MongoClient('mongo', 27017)
		self.db = connection['test']
		self.collection = self.db['items']

	def get_by_id(self, product_Id):
		product = self.collection.find_one({'_id': ObjectId(product_Id)})
		if product:
			return product
		return None

	def getProducts(self):
		products = self.collection.find()
		if not products:
			return []
		return products

	def delete(self, product_Id):
		deleted = self.collection.delete_one({'_id': ObjectId(product_Id)})
		return deleted
    
	def deleteAll(self):
		self.collection.remove({})
		return

	def update(self, product_Id, productData):
		updatedProduct = self.collection.update_one({"_id": ObjectId(product_Id)}, {"$set": productData}, upsert = False)
		return  ({"_id": product_Id, 'title': productData['title'], 'price':productData['price'], 'inventory_count': productData['inventory_count']})

	def addStudent(self, studentData):
		Id = self.collection.insert_one(studentData).inserted_id
		if not Id:
			return None
		return {'_id': Id , 'name' : studentData['name'] }
		
