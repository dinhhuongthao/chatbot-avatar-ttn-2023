
from fastapi import File, UploadFile, FastAPI
import shutil
import os
import cv2

import processing

app = FastAPI()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        filepath = os.path.join('./upload/', os.path.basename(file.filename))
        with open(filepath, 'wb') as f:
            shutil.copyfileobj(file.file, f)

        resImg = processing.addFrame(filepath)
        cv2.imshow("result", resImg)
        cv2.waitKey(0)

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

# run server: uvicorn index:app --reload
