from invoke import task


@task
def start(c):
    """
    Start the Flask development server.
    """
    c.run("poetry run flask --app src.app run --debug")


@task
def server(c):
    """
    Start the Flask development server.
    """
    c.run("gunicorn -w 4 'src.app:app'")
