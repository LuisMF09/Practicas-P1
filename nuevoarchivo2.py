from rembg import remove
from PIL import Image
input_path = "paisaje.jpg"
output_path = "paisaje2.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(output_path)
