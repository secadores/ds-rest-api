from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug, os
from pathlib import Path

app = Flask(__name__)
api = Api(app)
UPLOAD_FOLDER = 'upload'
parser = reqparse.RequestParser()
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

def malwareFound():
    print('malware detected')
    return {
        'message':'Infected file.',
        'status':'infected'
    }

def cleanFile(clean_file):
    print('clean file')
    os.remove(clean_file)
    return {
        'message':'Clean file.',
        'status':'clean'
    }

def noFile():
    print('no file was submited');
    return {
        'message':'File not found. Please verify your request.',
        'status':'error'
    }

def somethingWrong():
    print('something went wrong...')
    return {
        'data':'',
        'message':'Something went wrong with your request.',
        'status':'error'
    }

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        data = parser.parse_args()

        # If there is no file on the request
        if data['file'] == "":
            return noFile()

        # If there is a file
        toScan = data['file']
        if toScan:
            filename = 'to-scan'
            try:
                toScan.save(os.path.join(UPLOAD_FOLDER,filename))
                my_file = Path(UPLOAD_FOLDER + "/" + filename)
                # If file wasn't deleted
                if my_file.is_file():
                    return cleanFile(my_file)
                # if file was lately deleted
                else:
                    return malwareFound()
            # if file was deleted right away, raising exception
            except:
                return malwareFound()

        # Something went reeeeeaaally wrong
        return somethingWrong()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
