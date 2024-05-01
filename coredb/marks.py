import sqlite3
import uuid
from coredb.user import fetch_user_by_id , fetch_users_by_course
from coredb.subject import fetch_subject_by_id

def add_marks(marks_data):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()

    for mark in marks_data:
        mark_id = str(uuid.uuid4())
        cursor.execute('''INSERT INTO marks (id, user_id, subject, grades)
                          VALUES (?, ?, ?, ?)''',
                       (mark_id, mark['user_id'], mark['subject'], mark['grades']))
    db.commit()
    db.close()

def fetch_marks_by_user_id(user_id):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM marks WHERE user_id = ?''', (user_id,))
    marks = cursor.fetchall()
    db.close()

    # Convert fetched data into the specified format
    formatted_marks = []
    for mark in marks:
        mark_dict = {
            "id": mark[0],
            "user_id": mark[1],
            "subject": mark[2],
            "grades": mark[3]
        }
        formatted_marks.append(mark_dict)

    return formatted_marks

def fetch_marks_by_subject(subject):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM marks WHERE subject = ?''', (subject,))
    marks = cursor.fetchall()
    db.close()

    # Convert fetched data into the specified format
    formatted_marks = []
    for mark in marks:
        mark_dict = {
            "id": mark[0],
            "user": fetch_user_by_id(mark[1]),
            "subject": mark[2],
            "grades": mark[3]
        }
        formatted_marks.append(mark_dict)

    return formatted_marks


def fetch_pending_Marks_User(subject_id):

    course = fetch_subject_by_id(subject_id)

    all_users = fetch_users_by_course(course["course"])

    all_users = [user['id'] for user in all_users]

    grade_user_id = fetch_marks_by_subject(course["subject"])

    marked_users = [user['user']["id"] for user in grade_user_id]

    result = [x for x in all_users if x not in marked_users]

    user_records = []

    for user_id in result:
        user_record = fetch_user_by_id(user_id)
        user_records.append(user_record)

    return user_records










