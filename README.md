# OtpVerificationAPI

## About Project:
This is an API for OTP verification


## How to use

1. Send OTP to the user

```
GET https://api-otp.herokuapp.com/otp_varification/{phone_number}/{custom_message}
```
This API will return the OTP in JSON format and the same OTP will be sent to the provided phone number as well and this will happen simultaneously. 
You can match your OTP with the user entered OTP to verify the user identity.

## Example

To send OTP to the phone number 9978856438 with the custom message

```
GET https://api-otp.herokuapp.com/otp_varification/9978856438/This is your otp please do not share it with anyone
```

Above request will return following JSON  

```

{"otp":564783}

```

The following message will be sent to the provided number

```

This is your otp please do not share it with anyone 564783

```
## About Me:

[Click Here](https://hemendrakhatik.github.io/Portfolio/) to know about me.



