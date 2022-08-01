from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

users = [
    {"id": 1, "name": "Gus Gusman", "age": 23},
    {"id": 2, "name": "Bob Bobman", "age": 42},
    {"id": 3, "name": "Tim Timman", "age": 38},
    {"id": 4, "name": "Don Donman", "age": 55}
]

addresses = [
    {"id": 1, "userId": 1, "Type": "Home", "street": "123 Fake street", "country": "Canada"},
    {"id": 2, "userId": 1, "Type": "Business", "street": "124 Fake street", "country": "Mexico"},
    {"id": 3, "userId": 2, "Type": "Home", "street": "125 Fake street", "country": "Britain"},
    {"id": 4, "userId": 2, "Type": "Business", "street": "126 Fake street", "country": "Finland"},
    {"id": 5, "userId": 3, "Type": "Home", "street": "127 Fake street", "country": "Australia"},
    {"id": 6, "userId": 4, "Type": "Home", "street": "128 Fake street", "country": "Denmark"}
]

class Users(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        #query = conn.execute("select * from employees") # This line performs query and returns json result
        #return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        
        return users

class Addresses(Resource):
    def get(self):
        response = jsonify(addresses)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
@app.route('/addresses/<userId>')
def addressesByUserId(userId):
    usersAddresses = []
    for address in addresses:
        if(str(address["userId"]) == userId):
            usersAddresses.append(address)

    print(usersAddresses)
    return jsonify(usersAddresses)

#I haven't found documentation about what add_resourse actually does yet.
#So I'm not sure how to have the class handle addressesByUserId
api.add_resource(Users, '/users') # Route_1
api.add_resource(Addresses, '/addresses') # Route_1

#api.add_resource(Tracks, '/tracks') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

if __name__ == '__main__':
    app.debug = True
    app.run(port='5002')
