import pyotp

personal_code= pyotp.random_base32()

One_time_password = pyotp.TOTP(personal_code)

otp_code = One_time_password.now()
print(f"The OTP code: {otp_code}")

user_input = input("Enter the OTP code you received: ")

if One_time_password.verify(user_input):
    print("OTP verification successful.")
else:
    print("OTP verification failed.")
