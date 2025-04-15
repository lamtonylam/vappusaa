from invoke import task

@task
def start(c):
    """
    Start the Flask development server.
    """
    c.run("FLASK_APP=src.app FLASK_ENV=development poetry run flask run")