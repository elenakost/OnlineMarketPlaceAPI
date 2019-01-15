import Dao
class Model:
  
    def __init__(self, collection):
        self._id = str(collection['_id']) if '_id' in collection else None
        self.title = collection['title']
	self.price = collection['price']
	self.inventory_count = collection['inventory_count']      

    @staticmethod
    def get_by_id(product_Id):
        dao = Dao()
        product = dao.get_by_id(product_Id)
        if not product:
            return None
        return Model(product)
           
    @staticmethod
    def addProduct(productInfo):
        dao = Dao()
        new= dao.addProduct(productInfo)
        if not new:
          return None
        return Model(new)

    @staticmethod
    def deleteAll():
        dao=Dao()
        dao.deleteAll()
        return
        
    @staticmethod
    def purchase(product_Id):
        dao = Dao()
	item = dao.get(product_Id);
	if not item:
		return None
	if item["inventory_count"] <= 0:
		return None
	item["inventory_count"] = item["inventory_count"] -1
        purchase=dao.update(product_Id, productInfo)
        return purchase

    @staticmethod
    def getProducts():
        dao = Dao()
        allprod = dao.getProducts()
        products = []
        for s in allprod:
            products.append(Model(s))
        return products

