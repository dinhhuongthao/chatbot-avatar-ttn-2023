
from fastapi import File, UploadFile, FastAPI
import shutil
import os
import cv2

import processing

app = FastAPI()

# @app.post("/upload")
# def upload(file: UploadFile = File(...)):
#     try:
#         filepath = os.path.join('./upload/', os.path.basename(file.filename))
#         with open(filepath, 'wb') as f:
#             shutil.copyfileobj(file.file, f)
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         file.file.close()

#     return {"message": f"Successfully uploaded {file.filename}"}

# @app.post("/upload")
# def upload(file: UploadFile = File(...)):
#     try:
#         with open(file.filename, 'wb') as f:
#             while contents := file.file.read(1024 * 1024):
#                 f.write(contents)
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         file.file.close()

#     return {"message": f"Successfully uploaded {file.filename}"}


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

# run server: uvicorn main:app --reload
