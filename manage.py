from flask_script import Manager,Server
from app import create_app

app = create_app('default')

manager = Manager(app)

manager.add_command('server', Server)
@manager.command
def test():
    """Run the unit test."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity = 2).run(tests)

if __name__ == '__main__':
    manager.run()
