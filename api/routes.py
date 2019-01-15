from flask import Flask, jsonify, request
from api.models import records, Incident


app = Flask(__name__)

@app.route("/")
def home():
    """A welcoming route to my api"""

    return jsonify({
        'message': 'Welcome to mastula iReporter app.',
        'status': '200'
    }), 200

#API end point to create a red-flag record
@app.route("/api/v1/red-flags", methods=["POST"])
def create_redflag():
    if not request.json:
        return jsonify({
            "Error": "There is no data returned from the request",
            "status": 400
            }), 400
    data = request.get_json()
    if 'createdBy' not in data:
        return jsonify({'status': 400, 'Error': 'The information is missing'}), 400

    red_flag = Incident(
    		data["createdBy"], data["type"],
        	data["location"], data["status"], data["Images"],
        	data["Videos"], data["comment"]
       	   )
    records.append(
    	red_flag.format_record()
    	)
    if len(records) == 0:
    	return jsonify({
    		"status": 400, 
    		"Error": "Invalid request"
    		})
    return jsonify({
    	"status": 201,
    	"data": [{ 
        "id": red_flag._id,
        "Message": "Created red-flag record"
        }]}), 201



#API end point to fetch all records
@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_red_flags():
    if len(records) > 0:
        return jsonify({
        	"status": 200,
            "data": [red_flag for red_flag in records]
        	}), 200
    return jsonify({
    	"status": 400,
    	"Error": "There are no records"
   		})

#API end point to fetch a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["GET"])
def get_a_redflag(flag_id):
    red_flag_record= [red_flag for red_flag in records if red_flag['id'] == flag_id]
    if red_flag_record:
        return jsonify({
            "status": 200,
        	"redflag": red_flag_record
        	}), 200
    return jsonify({
    	"status": 404,
        "Error": " Invalid record"
    	})

# API end point to delete a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_red_flag(flag_id):
    red_flag_record = [flag for flag in records if flag['id'] == flag_id]
    if len(records) == 0:
        return jsonify({
        	"status": "400",
            "Error": "Invalid request"
        	}), 404
    records.remove(red_flag_record[0])
    return jsonify({
    	'Result': "record was deleted successfully"
    	}), 204




 