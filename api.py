from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
from io import BytesIO
from main import segment_everything
import hashlib
import time

app = FastAPI()

cache = {}
cache_ttl = {}

def generate_cache_key(image_bytes):
    return hashlib.sha256(image_bytes).hexdigest()

async def segment_image_async(contents):
    cache_key = generate_cache_key(contents)

    if cache_key in cache:
        if time.time() - cache_ttl[cache_key] > 3600:
            del cache[cache_key]
            del cache_ttl[cache_key]
        else:
            return cache[cache_key]
    
    image = Image.open(BytesIO(contents)).convert('RGB')

    segmented_image = segment_everything(image=image)

    img_byte_array = BytesIO()
    segmented_image.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)

    cache[cache_key] = img_byte_array.getvalue()
    cache_ttl[cache_key] = time.time()  

    return cache[cache_key]


@app.post("/segment-image/")
async def segment_image(file: UploadFile = File(...)):
    try:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Le fichier doit être une image.")

        contents = await file.read()

        segmented_image_bytes = await segment_image_async(contents)

        return StreamingResponse(BytesIO(segmented_image_bytes), media_type="image/png")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

