from flask import Flask, jsonify
import random
import requests
import json
import random 

app = Flask(__name__)

# This route accept two parameters receiver_phone_number and message 
@app.route("/otp_varification/<int:receiver_phone_number>/<string:message>",methods=['get'])
def otp_varification(receiver_phone_number,message):
  # generating six digits otp
  otp = random.randrange(1000,9999)
  api_key = "QSMJHMHYHX9C6SZDWMY5OIT14M06238F"
  secret_key = "0ZFVPHPK9QDTQ04U"
  usetype = "stage"
  sender_email = "hemendra.khatik010698@gmail.com"
  otp_message = message + " " + str(otp)
  sendGetRequest(URL, api_key, secret_key, usetype, receiver_phone_number, sender_email, otp_message)
  return jsonify(otp= otp)


URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendGetRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.get(reqUrl, req_params)    	

if __name__ == "__main__":
    app.run()   
