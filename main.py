import os
import string
import random

from flask import Flask, send_file, make_response, redirect, request
from flask_restful import Resource, Api
import filetype

app = Flask(__name__)
api = Api(app)

class File(Resource):
    def get(self, file_id):

        matching_file = None

        # find a file with a matching id
        for file in os.listdir():
            if file.startswith(file_id):
                matching_file = file

        # if we couldn't find a matching file then we return a 404
        if matching_file is None:
            return redirect("https://http.cat/404")

        return send_file(matching_file)

    def post(self, file_id):
        extension = filetype.guess(request.data).extension

        # create a random file id
        file_id = ""

        for i in range(4):

            file_id += random.choice(string.ascii_lowercase)

        with open(f"{file_id}.{extension}", "wb") as file:
            file.write(request.data)

        return f"media.vxny.net/{file_id}"

api.add_resource(File, '/<file_id>')

if __name__ == '__main__':
    app.run()