# Notes API

A simple RESTful API for managing notes built with FastAPI.

## Features

- Create new notes
- Retrieve all notes
- Retrieve a specific note by ID
- Update existing notes
- Delete notes

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd backNotasv1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server with:
```bash
python main.py
```
or
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation at `http://localhost:8000/docs`
- ReDoc documentation at `http://localhost:8000/redoc`

## API Endpoints

- `POST /notes/` - Create a new note
- `GET /notes/` - Get all notes
- `GET /notes/{note_id}` - Get a specific note
- `PUT /notes/{note_id}` - Update a note
- `DELETE /notes/{note_id}` - Delete a note

## Deployment

### Azure Deployment

1. Create an Azure Web App with Python runtime
2. Set up deployment from GitHub to Azure Web App
3. Configure the following in Azure Web App settings:
   - Add `WEBSITE_WEBDEPLOY_USE_SCM=true` to application settings
   - Set startup command: `python -m uvicorn main:app --host 0.0.0.0 --port 8000`

### GitHub

1. Initialize git repository:
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub

3. Push your code:
```bash
git remote add origin <your-repository-url>
git branch -M main
git push -u origin main
```

## License

MIT