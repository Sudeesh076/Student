from flask import Flask

from coredb.init import startDb
from routes.user import user
from routes.subject import subject

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(subject)

if __name__ == '__main__':
    startDb()
    app.run(debug=False)
