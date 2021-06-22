from flask import Flask,send_from_directory
app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('.','Automotive Security Timeline.html')

@app.route("/automotive/security/timeline.html",methods=['GET'])
def Automobile_Security_Timeline():
    return send_from_directory('.','Automotive Security Timeline.html')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port= 80,
        debug=True
    )