import pathlib
import pytesseract
from PIL import Image

BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR = BASE_DIR / "images"
img_1 = IMG_DIR / "testocr.png"

img = Image.open(img_1)

preds = pytesseract.image_to_string(img)
predictions = [x for x in preds.split("\n")]
print(predictions)