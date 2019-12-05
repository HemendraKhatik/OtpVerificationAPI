from flask import Flask

app = Flask(__name__)

@app.route("/otp_varification/<int:phone_number>",methods=['get'])
def otp_varification(phone_number):
	return "route is working"

if __name__ == "__main__":
    app.run()   