# kakao-chatbot

해당 튜토리얼은 카카오톡 사용자에 한해 간단하게 점심을 추천해주는 챗봇을 구현하기 위한 페이지입니다. '웨이버스 런치봇'은 Flask 라이브러리와 Heroku 무료 호스팅서버를 사용하였으며 DB는 Heroku에서 제공하는 Postgresql 기반으로 제공됩니다.

This tutorial is only for KaokaoTalk users to implement a simple chatbot that can be utilized for lunch recommendation. 'Wavus Lunchbot' is based on 'Flask' library and a free hosting server called 'Heroku', and its database is 'Postgresql' which is also a complimentary service that Heroku offers.  

## Getting Started
카카오톡 플러스친구 관리자 계정을 등록하기 아래 웹사이트에 접속하여 본인이 원하는 플러스친구 이름 및 사진을 설정합니다.

In order to register for KakaoTalk Plus Friend as an administrator, get access to the address below and created a certain name and picture for your own page. 
> https://center-pf.kakao.com

### prerequesites
초기 개발 환경을 구축하기 위해 아래의 절차를 따라합니다.

A step by step series of examples that tell you how to get a development env running

```
python -m pip install virtualenv
```

