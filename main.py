from flask import Flask

from coredb.init import startDb
from routes.user import user

app = Flask(__name__)
app.register_blueprint(user)

if __name__ == '__main__':
    startDb()
    app.run(debug=False)
