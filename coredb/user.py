import sqlite3
import uuid


def add_user(data):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    user_id = str(uuid.uuid4())

    cursor.execute('''INSERT INTO users (id, email, password, first_name, last_name, ph_number,type, course)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (user_id, data['email'], data['password'], data['first_name'], data['last_name'], data['ph_number'],
                    data['type'],data['course']))
    db.commit()
    db.close()


def fetch_user_by_id(user_id):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()

    cursor.execute("SELECT id, first_name, last_name, ph_number,email,type, course FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    db.close()

    if user is None:
        raise ValueError(f"User with ID {user_id} not found.")

    user_dict = {
        "id": user[0],
        "first_name": user[1],
        "last_name": user[2],
        "ph_number": user[3],
        "email" : user[4],
        "type" : user[5],
        "course": user[6],
    }

    return user_dict


def check_credentials_user(email, password):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    record = cursor.fetchone()

    if record and record[2] == password:
        db.close()
        return True, fetch_user_by_id(record[0])
    else:
        db.close()
        return False, "invalid"


def user_exists(email, ph_number):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM users WHERE email = ? OR ph_number = ?', (email, ph_number))
    count = cursor.fetchone()[0]

    db.close()

    return count > 0

def fetch_users_by_course(course):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()

    cursor.execute("SELECT id, first_name, last_name, ph_number, email, type, course FROM users WHERE course = ?", (course,))
    users = cursor.fetchall()

    db.close()

    if not users:
        raise ValueError(f"No users found for course {course}.")

    users_list = []
    for user in users:
        user_dict = {
            "id": user[0],
            "first_name": user[1],
            "last_name": user[2],
            "ph_number": user[3],
            "email": user[4],
            "type": user[5],
            "course": user[6],
        }
        users_list.append(user_dict)

    return users_list
