from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        #query = conn.execute("select * from employees") # This line performs query and returns json result
        #return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        return {'employees': 'test'}


api.add_resource(Employees, '/employees') # Route_1
#api.add_resource(Tracks, '/tracks') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

if __name__ == '__main__':
     app.run(port='5002')