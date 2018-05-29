import re
import requests
import urllib3
import json
import os
import sqlalchemy
import random
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class FoodList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	location = db.Column(db.String(120))
	weather = db.Column(db.String(20))
	
	def __init__(self, name, location, weather):
		self.name = name
		self.location = location
		self.weather = weather

	def __repr__(self):
		return '<Name %r>' % self.name
		
@app.route('/keyboard')
def keyboard():
	#초기 데이터 insert
	#insert_data()
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
				"text": "'웨이버스 런치봇'입니다. 친구 추가해 주셔서 감사합니다. \n 앞으로 점심은 저에게 맡겨주세요."
			}
		}
	elif content == u"도움말":
		dataSend = {
			"message": {
				"text": "웨이버스 직원분들을 위한 런치봇입니다.\n 배고프시면 '점심 추천'를 쳐주세요~"
			}
		}
	else:
		string = get_text(content)
		if string == "안녕":
			dataSend = {
				"message": {
					"text": "안녕하세요~저도 반갑습니다:)"
				}
			}
		elif string == "날씨":
			weather, temp = get_weather()
			dataSend = {
				"message": {
					"text": "오늘의 날씨는 " + str(weather) + "이고,\n온도는 " + str(temp) + "℃ 네요."
				}
			}	
		elif string == "점심":
			menu = get_menu()
			dataSend = {
				"message": {
					"text": "점심으로 오늘의 날씨에 어울리는 '" + str(menu) + "' 어때요?"
				}
			}
		else:
			dataSend = {
				"message": {
					"text": "잘 못알아듣겠습니다. 다른 식으로 시도해보세요~"
				}
			}
	return jsonify(dataSend)


def insert_data():
	db.session.add_all([
	FoodList('최우영스시', '서울 구로구 디지털로 288', '맑음'),
	FoodList('낭만부대찌개', '구로동 212-8 대륭포스트타워1차 B104호', '흐림'),
	FoodList('호우양꼬치', '서울 구로구 디지털로32나길 17-6', '비'),
	FoodList('멘무샤', '구로동 212-8 대륭포스트타워1차', '맑음'),
	FoodList('봉추찜닭', '구로동 188-25 지밸리비즈플라자', '맑음'),
	FoodList('포36거리', '구로동 212-8 대륭포스트타워1차 지하', '비'),
	FoodList('5 pane', '서울 구로구 디지털로26길 111', '맑음'),
	FoodList('홍콩반점', '서울 구로구 구로동 1125-15', '흐림'),
	FoodList('coro', '서울 구로구 디지털로32다길 30', '흐림'),
	FoodList('영호돈까스', '서울 구로구 시흥대로163길 21', '맑음')
    ])
	
	db.session.commit()
	
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

def get_menu():
	real_weather, temp = get_weather()
	menus = FoodList.query.filter_by(weather=real_weather)
	rand = random.randrange(0, menus.count()) 
	menu = db.session.query(menus)[rand]
	return menu.name


def get_text(text):
	openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
	accessKey = "15d93105-fa2b-474a-9b1f-1cabf928df1d"
	analysisCode = "morp"
	
	requestJson = {
		"access_key": accessKey,
		"argument": {
			"text": text,
			"analysis_code": analysisCode
		}
	}
	
	http = urllib3.PoolManager()
	response = http.request(
		"POST",
		openApiURL,
		headers={"Content-Type": "application/json; charset=UTF-8"},
		body=json.dumps(requestJson)
	)
	
	data = json.loads(str(response.data, "utf-8"))
	data1 = data["return_object"]["sentence"]
	b = data1[0]['morp']
	if [element for element in b if element['lemma'] == '안녕']:
		result = '안녕'
	elif [element for element in b if element['lemma'] == '날씨']:
		result = '날씨'
	elif [element for element in b if element['lemma'] == '점심']:
		result = '점심'
	else:
		result = '미등록'
	return result
	
	
if __name__ == '__main__':
	app.run()