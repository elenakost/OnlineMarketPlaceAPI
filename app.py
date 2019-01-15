from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request, abort
from model import Model
from validator import validator, MultipleInvalid
import json
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('price')
parser.add_argument('inventory_count')

class Item(Resource):
    # get a product by id
    def get(self, product_id):
        try:
            validator.validateId(product_id)
            product = Model.get_by_title(product_id) 
        except MultipleInvalid as e:
            return str(e), 400
        except:
           return 'error', 500
        if not product:
            abort(404, message = "Getting product {} failed".format(product_id))
        _return = jsonify(product.__dict__)
        _return.status_code = 200
        return _return      
        
    # purchase a product by id (reduce count by 1)
    def delete(self, product_id):
        try:
            validator.validateId(product_id)
            deleted = Model.purchase(product_id)          
        except MultipleInvalid as e:
            return str(e), 400
        except:
            return 'error', 500
        if not deleted:
            abort(404, message = "Deleting product {} failed".format(product_id))
        return '', 204 
    
class ItemList(Resource):
    # get all items in inventory 
    def get(self):
        try:
            items = Model.getProducts() 
        except:
            return 'an error', 500
        if not items:
            abort(404, message = "Getting all items failed")
        jsonlist = []
        for item in items:
            jsonlist.append(item.__dict__)
        return jsonlist, 200
        
    # add item to inventory    
    def post(self):
        args = parser.parse_args()
        try:
            validator.validateData(args)
            item = Model.addProduct(args)        
        except MultipleInvalid as e:
            return str(e), 400
        except:
            return 'error', 500
        _return = jsonify(item.__dict__)
        _return.status_code = 201
        return _return    

    # delete inventory
    def delete(self):
        try:
            deleted = Model.deleteAll()
        except:
            return 'error', 500
        return 'deleted', 204

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<item_id>')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
