import glob

import piexif
import pillow_heif
from PIL import Image

pillow_heif.register_heif_opener()


def convert_heic_to_jpeg(filename):
    image = Image.open(filename)
    image.save(filename.replace(".HEIC.heif", ".jpeg"))
    return image


def update_date(imagename, new_date):
    exif_dict = piexif.load(imagename)
    exif_dict["0th"][piexif.ImageIFD.DateTime] = new_date
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, imagename)


folder_path = "C:/Users/jblam/Pictures/new"

for filename in glob.glob(folder_path + "/*.HEIC.heif"):
    print(filename)
    image = convert_heic_to_jpeg(filename)
    new_date = image.getexif()[piexif.ImageIFD.DateTime]
    imagename = filename.replace(".HEIC.heif", ".jpeg")
    update_date(imagename, new_date)
