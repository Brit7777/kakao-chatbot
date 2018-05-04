from flask import Flask, request, jsonify

app = Flask(__name__)
	
@app.route('/message', methods=['POST'])
def Message():
	dataReceive = request.get_json()
	content = dataReceive['content']
 
 
	if content == u"시작하기":
		dataSend = {
			"message": {
				"text": "안녕하세요!웨이버스 런치봇입니다. 무엇을 도와드릴까요?"
			}
		}
	return jsonify(dataSend)
	
if __name__ == '__main__':
	app.run()