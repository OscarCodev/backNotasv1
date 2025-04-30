from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Api de notas UNSCH",
    description="A simple API for managing notes",
    version="1.0.0"
)

class Note(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Mock database
notes_db: List[Note] = []
# Counter for note IDs
note_counter = 1

@app.post("/notes/", response_model=Note, status_code=201)
def create_note(note: Note):
    global note_counter
    note.id = note_counter
    note.created_at = datetime.now()
    note.updated_at = datetime.now()
    notes_db.append(note)
    note_counter += 1
    return note

@app.get("/notes/", response_model=List[Note])
def get_all_notes():
    return notes_db

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    note = next((note for note in notes_db if note.id == note_id), None)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, updated_note: Note):
    note_index = next((index for index, note in enumerate(notes_db) if note.id == note_id), None)
    if note_index is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    current_note = notes_db[note_index]
    update_data = updated_note.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    update_data["id"] = note_id
    update_data["created_at"] = current_note.created_at
    
    notes_db[note_index] = Note(**update_data)
    return notes_db[note_index]

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    note_index = next((index for index, note in enumerate(notes_db) if note.id == note_id), None)
    if note_index is None:
        raise HTTPException(status_code=404, detail="Note not found")
    notes_db.pop(note_index)
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)