import sys

import pyperclip
import requests as r

# upload the passed file
file_path = sys.argv[1]

with open(file_path, "rb") as file:
    f = file.read()

resp = r.post("http://127.0.0.1:5000/d", data=f)

pyperclip.copy(resp.text)

