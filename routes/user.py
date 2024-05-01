from flask import Blueprint, request, jsonify
from coredb.user import add_user, user_exists, check_credentials_user

user = Blueprint('user', __name__)


@user.route('/user', methods=['POST'])
def new_user():
    try:
        data = request.json
        if 'email' in data and 'password' in data and 'first_name' in data and 'last_name' in data and 'ph_number' in data and 'type' in data and 'course' in data:
            if not user_exists(data['email'], data['ph_number']):
                validate_course_type(data['course'])
                validate_user_type(data['type'])
                add_user(data)
                return jsonify({"message": "User record created successfully"}), 201
            else:
                return jsonify({"error": "User with the same email or phone number already exists"}), 409
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user.route('/login/user', methods=['POST'])
def loginUser():
    try:
        data = request.get_json()

        if 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required fields"}), 400

        email = data['email']
        password = data['password']

        authenticated, data = check_credentials_user(email, password)

        if authenticated:
            return jsonify(data)
        else:
            return jsonify(data), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def validate_course_type(course_type):
    valid_course = ["Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Computer Engineering", "Biomedical Engineering"]
    print(course_type)
    if course_type not in valid_course:
        raise ValueError(f"Invalid course type. Allowed values are: {', '.join(valid_course)}")

def validate_user_type(user_type):
    valid_user = ["Student","Faculty"]

    if user_type not in valid_user:
        raise ValueError(f"Invalid user type. Allowed values are: {', '.join(valid_user)}")
