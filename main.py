import os
from flask import *
app = Flask(__name__, static_folder="/")

RESOURCE_DIR = os.path.join(os.getcwd(), "resources")

@app.route('/jp_release_android.env')
def get_env_file():
    try:
        return send_from_directory(RESOURCE_DIR, 'jp_release_android.env')
    except FileNotFoundError:
        abort(404)
@app.route('/jp_release_android.mapping')
def get_mapping_file():
    try:
        return send_from_directory(RESOURCE_DIR, 'jp_release_android.mapping')
    except FileNotFoundError:
        abort(404)


@app.route("/getversion")
def return_version():
    return "2.0.0.20042164" # 最新は2.0.1.20043076だけど見つからないので2.0固定

@app.route("/account/user/regist", methods=['POST'])
def user_regist():
    user_json = {
        "Ecode": "",
        "Value": {
              "UID": 123123123,
              "Token": "abc",
              "LoginToken": "bcd",
              "Phone": 18252729078,
              "Email": "i@smyhw.online",
              "ThirdParty": 0, 
              "UserType": 2, 
              "IDCardStatus": 1,
              "OnlineTime": 111,
              "OnlineStep": 2,
              "ZoneInfo": [
                  {
                      "Platform": 0,
                      "ZID": 0,
                      "ZoneName": "qwq",
                      "ZoneStatus": 1,
                      "ServerIP": "127.0.0.1",
                      "Sort": 1
                  }
              ]
          }
    }
    return jsonify(user_json)

@app.route("/account/user/login", methods=['POST'])
def user_login():
    user_json = {
        "Ecode": "",
        "Value": {
              "UID": 123123123,
              "Token": "abc",
              "LoginToken": "bcd",
              "Phone": 18252729078,
              "Email": "i@smyhw.online",
              "ThirdParty": 0, 
              "UserType": 2, 
              "IDCardStatus": 1,
              "OnlineTime": 111,
              "OnlineStep": 2,
              "ZoneInfo": [
                  {
                      "Platform": 0,
                      "ZID": 0,
                      "ZoneName": "qwq",
                      "ZoneStatus": 1,
                      "ServerIP": "127.0.0.1",
                      "Sort": 1
                  }
              ]
          }
    }
    return jsonify(user_json)


@app.route("/account/user/tokenlogin", methods=['POST'])
def token_login():
    user_json = {
        "Ecode": "",
        "Value": {
              "UID": 123123123,
              "Token": "abc",
              "LoginToken": "bcd",
              "Phone": 18252729078,
              "Email": "i@smyhw.online",
              "ThirdParty": 0, 
              "UserType": 2, 
              "IDCardStatus": 1,
              "OnlineTime": 111,
              "OnlineStep": 2,
              "ZoneInfo": [
                  {
                      "Platform": 0,
                      "ZID": 0,
                      "ZoneName": "qwq",
                      "ZoneStatus": 1,
                      "ServerIP": "127.0.0.1",
                      "Sort": 1
                  }
              ]
          }
    }
    return jsonify(user_json)


@app.route("/account/test/ok",methods=['POST'])
def account_ok():
    return "OK"

@app.route("/Notice/gameContent",methods=['GET'])
def gameContent():
    return {
        "Ecode": "",
        "Value": {
            "Content": "123123",
            "Title": "标题"
        },
    }

@app.route("/Notice/fetchContent",methods=['POST'])
def fetchContent():
    return "テスト"

if __name__ == '__main__':
  app.run(port=8080, debug=True)