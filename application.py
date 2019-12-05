from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/otp_varification/<int:phone_number>",methods=['get'])
def otp_varification(phone_number):
	# generating six digits otp
	otp = random.randrange(100000,999999)
	return jsonify(otp= otp)

if __name__ == "__main__":
    app.run()   