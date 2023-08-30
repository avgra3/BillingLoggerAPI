# Python API

## Packages used:

    - FastAPI
    - uvicorn
    - SQLAlchemy

## Steps to start server:

Run the below from the [api](./api/) directory

```bash
uvicorn main:app --reload --port 8000
```
or from the [parent directory](..) of the api:

```bash
uvicorn main:app --reload --reload-dir ./api --app-dir ./api --port 8000
```


## Documentation

[Fast API]

<!-- References -->
[AvaloniaUI]: https://docs.avaloniaui.net/
[Fast API]: https://fastapi.tiangolo.com/
