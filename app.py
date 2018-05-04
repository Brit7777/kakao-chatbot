from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
	dataSend = {
	"type" : "buttons",
		"buttons" : ["시작하기", "도움말"]
	}
 
	return jsonify(dataSend)

	
@app.route('/message', methods=['POST'])
def Message():
	dataReceive = request.get_json()
	content = dataReceive['content']
 
 
	if content == u"시작하기":
		dataSend = {
			"message": {
				"text": "안녕"
			}
		}
	return jsonify(dataSend)
	
if __name__ == '__main__':
	app.run()