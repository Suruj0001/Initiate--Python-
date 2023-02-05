from PIL import Image
import glob

path = r"C:\Users\suruj\.spyder-py3\photo-folder\*"

for file in glob.glob(path):
    print(file)
    pil = Image.open(file)
    a = pil.rotate(45 , expand=True)
    a.save(r"C:\Users\suruj\.spyder-py3\rotate-photo-folder\roate.png")