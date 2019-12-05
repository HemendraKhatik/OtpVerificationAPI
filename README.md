# OtpVerificationAPI

## About Project:
This is an API for OTP verification


## How to use

1. Send OTP to the user

```
GET https://api-otp.herokuapp.com/otp_varification/{phone_number}
```
This API will return the OTP in JSON format and same otp will be sent to the provided phone number as well and this will happend simultaneously. 
You can match your OTP with the user entered OTP to verify the user identity.

## Example

To send OTP to the phone number 9978856438

```
GET https://api-otp.herokuapp.com/otp_varification/9978856438
```

This will return 

```
{"otp":564783}
```

## About Me:

[Click Here](https://hemendrakhatik.github.io/Portfolio/) to know about me.



