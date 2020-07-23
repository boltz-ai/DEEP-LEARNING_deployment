# Developed by Mirko J. Rodríguez mirko.rodriguezm@gmail.com

# ------------------------
# REST service via FastAPI
# ------------------------

#Import FastAPI libraries
from fastapi import FastAPI, File, UploadFile
from typing import Optional

#Import Tensorflow image
from tensorflow.keras.preprocessing import image

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

#Main definition for FastAPI
app = FastAPI()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Define a default route
@app.get('/')
def main_page():
    return 'REST service is active via FastAPI'

@app.post("/model/predict/")
async def predict(file: UploadFile = File(...)):
    filename = file.filename
    if file and allowed_file(filename):
        print("\nfilename:",filename)
        contents = await file.read()
        print("\ncontents:",contents)
        image_to_predict = image.load_img(filename??, target_size=(224, 224))

    return {"filename": file.filename}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
