# DS-Rest-API

## Overview

This personal and non supported project is a Proof of Concept on how Deep Security can be used to provide "Scan as a Service" through HTTP, on a Rest-like implementation.

## How it works

- A Python 3 application runs a web server (Flask) waiting for Post calls on the '/' endpoint.
- Whenever a file is received, it will be saved in disk.
- Deep Security Agent will immediately delete the file if malicious.
- A respose is sent back to the call.
- If the file was deleted, the web server returns a 'infected' status
- IF the file wasn't deleted, the web server returns a 'clean' status

## How to run it

*Important:* Deep Security agent must be installed, activaded and with a policy applied that is able to, in real time, scan the folder where the application is runned and its subfolders.

Make sure to have Python 3.6+ installed and clone the repository.

`pip3 install -r requirements.txt`

`python3 app.py`

## How to use it

Make a post request with the file to be scanned as a value to the key "file" in its body. The application, by default, listens at the port '5000'.

### Example

`
curl -X POST http://$SERVER:5000/ -H 'content-type: multipart/form-data'   -F 'file=@/path/to/file
`

## Possible responses

### Malware detected

`{
      'message':'Infected file.',
      'status':'infected'
  }`

### Clean file

`{
      'message':'Clean file.',
      'status':'clean'
  }`

### File not submited

`{
      'message':'File not found. Please verify your request.',
      'status':'error'
  }`

### Unknown error

`{
      'message':'Something went wrong with your request.',
      'status':'error'
  }`
