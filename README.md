# kakao-chatbot

해당 튜토리얼은 카카오톡 사용자에 한해 간단하게 점심을 추천해주는 챗봇을 구현하기 위한 페이지입니다. '웨이버스 런치봇'은 Flask 라이브러리와 Heroku 무료 호스팅서버를 사용하였으며 DB는 Heroku에서 제공하는 Postgresql 기반으로 제공됩니다. 이 뿐만 아니라, 인공지능적 요소를 결합하기 위해 언어 분석에 사용되는 공공 인공지능 오픈 API '엑소브레인'을 적용하여 특정 단어가 포함되어 있는 문장에 대한 대답 과정을 구현하였습니다. 

This tutorial is only for KaokaoTalk users to implement a simple chatbot that can be utilized for lunch recommendation. 'Wavus Lunchbot' is based on 'Flask' library and a free hosting server called 'Heroku', and its database is 'Postgresql' which is also a complimentary service that Heroku offers. Moreover, taking 'AI' into account, the public Open Source API 'Exobrain' has taken part in analyzing the sentence coming from the user so that lunchbot can respond to the sentence which includes a certain word. 

## Getting Started
카카오톡 플러스친구 관리자 계정을 등록하기 아래 웹사이트에 접속하여 본인이 원하는 플러스친구 이름 및 사진을 설정합니다.

In order to register for KakaoTalk Plus Friend as an administrator, get access to the address below and created a certain name and picture for your own page. 
> https://center-pf.kakao.com

### prerequesites
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
//type id
//type pwd
```
Git에서 사용 가능한 Heroku 저장소 형성
create Heroku repository for Git
```
$ heroku create
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

파이썬 언어를 이용한 예제 코드 아래와 같습니다.

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
