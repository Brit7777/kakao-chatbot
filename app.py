from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

@app.route('/keyboard')
def keyboard(requests):
	return JasonResponse({
		'type' : 'text'
	})

	
@app.route('/message', methods=['POST'])
def Message(request):
	message = ((request.body).decode('utf-8'))
	if(message.find(u"식당")>-1 or message.find(u"배고파")>-1):
		return JasonResponse({
		'message' : {
			'text':'선택해주세요'
		},
		'keyboard : {
			"type":"buttons"
			, "buttons" : ["중식", "양식", "한식"]
		}
		})
	


		
if __name__ == '__main__':
	app.run()