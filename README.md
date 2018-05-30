# kakao-chatbot

해당 튜토리얼은 카카오톡 사용자에 한해 간단하게 점심을 추천해주는 챗봇을 구현하기 위한 페이지입니다. '웨이버스 런치봇'은 Flask 라이브러리와 Heroku 무료 호스팅서버를 사용하였으며 DB는 Heroku에서 제공하는 Postgresql 기반으로 제공됩니다. 이 뿐만 아니라, 인공지능적 요소를 결합하기 위해 언어 분석에 사용되는 공공 인공지능 오픈 API '엑소브레인'을 적용하여 특정 단어가 포함되어 있는 문장에 대한 대답 과정을 구현하였습니다. '웨이버스 런치봇'을 사용해보고 싶다면 카카오톡 플러스 친구에서 친구 추가해주세요:)

This tutorial is only for KaokaoTalk users to implement a simple chatbot that can be utilized for lunch recommendation. 'Wavus Lunchbot' is based on 'Flask' library and a free hosting server called 'Heroku', and its database is 'Postgresql' which is also a complimentary service that Heroku offers. Moreover, taking 'AI' into account, the public Open Source API 'Exobrain' has taken part in analyzing the sentence coming from the user so that lunchbot can respond to the sentence which contains a certain word. If you want to take a look at my lunchbot, search '웨이버스 런치봇' in Kakao and add me:)

## Getting Started
카카오톡 플러스친구 관리자 계정을 등록하기 아래 웹사이트에 접속하여 본인이 원하는 플러스친구 이름 및 사진을 설정합니다.

In order to register for KakaoTalk Plus Friend as an administrator, get access to the address below and created a certain name and picture for your own page. 
> https://center-pf.kakao.com

### prerequisites
초기 개발 환경을 구축하기 위해 아래의 절차를 따라합니다.

A step by step series of examples that tell you how to get a development env running

```
$ python -m pip install virtualenv

//app 코드가 있는 폴더로 이동
//move to the folder that contains app.py
$ virtualenv venv
$ cd venv/Scripts
$ .\activate
```
requirements.txt에 있는 라이브러리 모두 설치해야 합니다.

You must install all the libraries mentioned in 'requirements.txt' file.
```
click==6.7
Flask==1.0.2
Flask-SQLAlchemy==2.3.2
gunicorn==19.8.1
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
psycopg2-binary==2.7.4
SQLAlchemy==1.2.7
Werkzeug==0.14.1
requests==2.18.4
```
## Deployment
1. Heroku 서버를 사용하기 위한 계정을 만들어줍니다.

Create an account for Heroku server from the link below.
> https://dashboard.heroku.com/apps

2. Heroku CLI(command line interface)를 설치합니다.

Download Heroku CLI(command line interface) from the website below.
> https://devcenter.heroku.com/

3. Heroku CLI에서 사용되는 중요 명령어들을 익힙니다.

cmd창에서 Heroku 접속
Access to Heroku through cmd
```
$ heroku login
#type id
#type pwd
```
Git에서 사용 가능한 Heroku 저장소 형성
create Heroku repository for Git
```
$ heroku create
```
연동된 DB url 확인
check for the database url connected to the repository
```
$ heroku config
//내용
=== mighty-spire-71391 Config Vars
DATABASE_URL: postgres://mptqompjxuqoky:64a85490a0517fd0ab6a2b27f87be93baac5726829b8f62d5fc87d29ef2bd927@ec2-54-204-46-236.compute-1.amazonaws.com:5432/d7ub5amthegeme
```
4. Heroku 저장소에 코드를 올리기 위해 아래의 절차를 밟습니다. 

A step by step series of examples that tell you how to update the modified code to Heroku repository

```
$ git add --all
$ git commit -m "commit"
$ git push heroku master
//to check log details
$ heroku logs --tail -a 저장소 이름
```
## Using Exobrain API (optional)

아래의 사이트에서 엑소브레인 API 사용 신청을 합니다.

Apply for the access token from the website. 
> http://aiopen.etri.re.kr/

exobrain.py 예제 코드 아래와 같습니다.

This is the example code making use of API in python.

```
    #-*- coding:utf-8 -*-
    import urllib3
    import json

    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
    accessKey = "YOUR_ACCESS_KEY"

`analysisCode =` `"morp"`

    text = "YOUR_SENTENCE"

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
    
    print("[responseCode] " + str(response.status))
    print("[responBody]")
    print(str(response.data,"utf-8"))
```

## Connection to DataBase
1. heroku 사이트 내 addons에서 'Heroku Postgres'를 추가해줍니다.

Look for the icon with 'Heroku Postgres' from addons in heroku website and add it to your repository.
> https://elements.heroku.com/addons 
2. 'heroku config' 명령어를 통해 확인한 주소를 환경변수로 설정해줍니다. 

Set the environment path for DB using the url address from 'heroku config' command line.
```
$ set DATABASE_URL=postgres://자기 url 주소
```
3. app.py 파일 내에 아래의 코드를 추가해주세요.

add the following code to the top of 'app.py' file.
```
import os
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```
4. 아래의 절차를 따라 커밋 후 테이블을 생성해봅니다.

Follow the instruction below in order to commit the changes and create a brand new table.
```
$ git commit -a -m "added DB boilerplate"
$ git push heroku master
$ heroku run python
>>> from app import db
>>> db.create_all()
>>> db.session.commit()
```
5. 생성된 테이블을 아래와 같이 SQLAlchemy를 활용하여 구성해줍니다.

Now construct the table with SQLAlchemy by utilizing the following code.
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name
 
 ```
데이터 추가 
Inserting data
```
user = User('John Doe', 'john.doe@example.com')
db.session.add(user)
db.session.commit()
 
 ```
 데이터 가져오기
 Selecting all data
 ```
 all_users = User.query.all()
 ```
 데이터 지우기
 deleting data
 ```
user = User('John Doe', 'john.doe@example.com')
db.session.delete(user)
db.session.commit()
 ```
 
 ## Keeping Heroku awake
 setInterval.js를 통해 Heroku 서버를 1분마다 깨워주도록 합니다. 
 
 With the help of setInterval.js file, wake Heroku server up every minute.
