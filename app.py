from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
	dataSend = {
		"type" : "buttons",
		"buttons" : ["시작하기","도움말"]
	}
	return jsonify(dataSend)

	
@app.route('/message', methods=['POST'])
def Message():
	dataReceive = request.get_json()
	content = dataReceive['content']
 
	if content == u"시작하기":
		dataSend = {
			"message": {
				"text": "안녕하세요~웨이버스 런치봇입니다!무엇을 도와드릴까요?"
			}
		}
	elif content == u"날씨":
		weather, temp = get_weather();
		dataSend = {
			"message": {
				"text": "오늘의 날씨는 " + str(weather) + "이고,\n온도는 " + str(temp) + "℃ 네요."
			}
		}
	return jsonify(dataSend)


def get_weather():
	regionCode = '09530540'
	url = "https://m.weather.naver.com/m/main.nhn?regionCode=" + regionCode
	summary_regex = r"weather_set_summary\">(.+?)<br>"
	nowTemp_regex = r"degree_code full\">(.+?)</em>"
	response = requests.get(url)
	data = response.text
	summary = re.search(summary_regex, data)
	nowTemp = re.search(nowTemp_regex, data)
	
	return summary.group(1), nowTemp.group(1)
		
if __name__ == '__main__':
	app.run()