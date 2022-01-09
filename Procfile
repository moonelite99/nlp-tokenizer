web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
worker: uvicorn main:app --reload
