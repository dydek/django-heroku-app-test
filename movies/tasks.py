from heroku_app.celery import app


@app.task(bind=True)
def movies_task(self):
    print('Request: {0!r}'.format(self.request))
