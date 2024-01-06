from flask import Flask, jsonify, request, abort
from shoplistDAO import shoplistDAO

#app = Flask(__name__, static_url_path='', static_folder='.')
app = Flask(__name__, static_url_path='', static_folder='staticpages')

#app = Flask(__name__)

@app.route('/')
def index():
    return ('OK')

#curl "http://127.0.0.1:5000/items"
@app.route('/items')
def getAll():
    #print("in getall")
    results = shoplistDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/items/2"
@app.route('/items/<int:id>')
def findById(id):
    foundItem = shoplistDAO.findByID(id)
    return jsonify(foundItem)


#curl  -i -H "Content-Type:application/json" -X POST -d "{\"prod_name\":\"hello\",\"shop\":\"someone\",\"quantity\":123}" http://127.0.0.1:5000/items
@app.route('/items', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    item = {
        "prod_name": request.json['prod_name'],
        "shop": request.json['shop'],
        "quantity": request.json['quantity'],
    }
    values =(item['prod_name'],item['shop'],item['quantity'])
    newId = shoplistDAO.create(values)
    item['id'] = newId
    return jsonify(item)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"prod_name\":\"hello\",\"shop\":\"someone\",\"quantity\":123}" http://127.0.0.1:5000/items/1
@app.route('/items/<int:id>', methods=['PUT'])
def update(id):
    foundItem = shoplistDAO.findByID(id)
    if not foundItem:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'quantity' in reqJson and type(reqJson['quantity']) is not int:
        abort(400)
    if 'prod_name' in reqJson:
        foundItem['prod_name'] = reqJson['prod_name']
    if 'Author' in reqJson:
        foundItem['shop'] = reqJson['shop']
    if 'quantity' in reqJson:
        foundItem['quantity'] = reqJson['quantity']
    values = (foundItem['prod_name'],foundItem['shop'],foundItem['quantity'],foundItem['id'])
    shoplistDAO.update(values)
    return jsonify(foundItem)
        

    

@app.route('/items/<int:id>' , methods=['DELETE'])
def delete(id):
    shoplistDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)