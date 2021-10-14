import sys

# Library to handle copy to clipboard
import pyperclip

# Library to handle JWT requests
import jwt


def decodeJWT():
    token = sys.argv[1]
    copy = False
    if len(sys.argv) == 3:
        copy = True

    decoded_token = jwt.decode(token, options={"verify_signature": False})

    print("\n\n\n")
    print(decoded_token)

    if copy:
        if 'surveyId' in decoded_token:
            pyperclip.copy(decoded_token['surveyId'])
        else:
            pyperclip.copy(str(decoded_token))


if __name__ == '__main__':
    decodeJWT()
