from flask import Blueprint, request, jsonify
from coredb.marks import add_marks, fetch_marks_by_user_id, fetch_marks_by_subject ,fetch_pending_Marks_User

marks = Blueprint('marks', __name__)

@marks.route('/marks', methods=['POST'])
def add_marks_route():
    try:
        marks_data = request.json
        if marks_data:
            add_marks(marks_data)
            return jsonify({"message": "Marks records added successfully"}), 201
        else:
            return jsonify({"error": "No data provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@marks.route('/marks/<user_id>', methods=['GET'])
def get_marks_by_user_id(user_id):
    try:
        marks = fetch_marks_by_user_id(user_id)
        if marks:
            return jsonify({"marks": marks}), 200
        else:
            return jsonify({"message": "No marks found for the user ID"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@marks.route('/marks/subject/<subject>', methods=['GET'])
def get_marks_by_subject(subject):
    try:
        marks = fetch_marks_by_subject(subject)
        if marks:
            return jsonify({"marks": marks}), 200
        else:
            return jsonify({"message": "No marks found for the subject"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@marks.route('/marks/pending/<subject_id>', methods=['GET'])
def get_pending_marks_by_subject(subject_id):
    try:
        users = fetch_pending_Marks_User(subject_id)
        if users:
            return jsonify({"users": users}), 200
        else:
            return jsonify({"message": "No users found for the subject"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
