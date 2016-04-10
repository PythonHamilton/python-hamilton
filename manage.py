from flask.ext.script import Manager
from python_hamilton import create_app


manager = Manager(create_app)
manager.add_option("-c", "--config", dest="config", required=False)


if __name__ == "__main__":
    manager.run()
