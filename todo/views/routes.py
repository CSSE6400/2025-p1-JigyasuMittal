from flask import Blueprint
from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/health')
def health():
    return jsonify({"status": "ok"})



@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify([{
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }])
@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    })

@api.route('/todos', methods=['POST'])
def create_todo():
    return jsonify({
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }), 201  # HTTP 201 Created

@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()  # Get updated data from the request body
    
    if not data:
        return jsonify({"error": "Invalid request, no data provided"}), 400

    return jsonify({
        "id": id,
        "title": data.get("title", "Watch CSSE6400 Lecture"),
        "description": data.get("description", "Watch the CSSE6400 lecture on ECHO360 for week 1"),
        "completed": data.get("completed", True),
        "deadline_at": data.get("deadline_at", "2023-02-27T00:00:00"),
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2025-02-28T00:00:00"  # Simulate update time
    }), 200  # HTTP 200 OK

@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    })
