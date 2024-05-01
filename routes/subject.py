from flask import Blueprint, request, jsonify
from routes.user import validate_course_type
from coredb.subject import add_subject, fetch_subject_by_id,fetch_subject_by_course


subject = Blueprint('subject', __name__)

@subject.route('/subject', methods=['POST'])
def add_course():
    try:
        data = request.json
        if 'subject' in data and 'semester' in data and 'description' in data and 'course' in data:
            validate_course_type(data['course'])
            return jsonify(add_subject(data)), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@subject.route('/subject/<string:subject_id>', methods=['GET'])
def get_subject_by_id(subject_id):
    try:
        subject_info = fetch_subject_by_id(subject_id)
        return jsonify(subject_info), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@subject.route('/subject/course/<string:course>', methods=['GET'])
def get_subjects_by_course(course):
    try:
        subjects_for_course = fetch_subject_by_course(course)
        return jsonify(subjects_for_course), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
