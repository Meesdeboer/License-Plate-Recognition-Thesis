import os
from PIL import Image

dir = "../../../test_images/normal_cars"

for file in os.listdir(dir):
    print(file)
    if file.count("-") != 2:
        img = Image.open(os.path.join(dir, file))
        img.show()
        name = input("Enter name: ")
        img.save(f"../../../test_images/normal_cars/{name}.jpg")
        os.remove(os.path.join(dir, file))
        img.close()

