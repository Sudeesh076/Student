import sqlite3
import uuid

# def add_subject(data):
#     db = sqlite3.connect("student.db")
#     cursor = db.cursor()
#     subject_id = str(uuid.uuid4())
#
#     cursor.execute('''INSERT INTO subject (id, subject, semester, description, course)
#                       VALUES (?, ?, ?, ?, ?)''',
#                    (subject_id, data['subject'], data['semester'], data['description'], data['course']))
#     db.commit()
#     db.close()

def add_subject(data):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()
    subject_id = str(uuid.uuid4())

    cursor.execute('''INSERT INTO subject (id, subject, semester, description, course)
                      VALUES (?, ?, ?, ?, ?)''',
                   (subject_id, data['subject'], data['semester'], data['description'], data['course']))
    db.commit()

    cursor.execute("SELECT * FROM subject WHERE id=?", (subject_id,))
    new_subject = cursor.fetchone()

    db.close()

    return new_subject


def fetch_subject_by_id(subject_id):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()

    cursor.execute("SELECT id, subject, semester, description, course FROM subject WHERE id = ?", (subject_id,))
    subject = cursor.fetchone()

    db.close()

    if subject is None:
        raise ValueError(f"Subject with ID {subject_id} not found.")

    subject_dict = {
        "id": subject[0],
        "subject": subject[1],
        "semester": subject[2],
        "description": subject[3],
        "course": subject[4],
    }

    return subject_dict

def fetch_subject_by_course(course):
    db = sqlite3.connect("student.db")
    cursor = db.cursor()

    cursor.execute("SELECT id, subject, semester, description FROM subject WHERE course = ?", (course,))
    subjects = cursor.fetchall()

    db.close()

    if not subjects:
        raise ValueError(f"No subjects found for course {course}.")

    subjects_list = []
    for subject in subjects:
        subject_dict = {
            "id": subject[0],
            "subject": subject[1],
            "semester": subject[2],
            "description": subject[3]
        }
        subjects_list.append(subject_dict)

    return subjects_list
