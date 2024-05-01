from flask import Flask

from coredb.init import startDb
from routes.user import user
from routes.subject import subject
from routes.marks import marks

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(subject)
app.register_blueprint(marks)

if __name__ == '__main__':
    startDb()
    app.run(debug=False)
