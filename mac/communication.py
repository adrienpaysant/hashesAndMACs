import hmac
import hashlib

MESSAGE = ''
DIGEST = ''

def send_message(msg, msg_integrity = True):
    global MESSAGE
    if msg_integrity:
        MESSAGE = msg
    else :
        MESSAGE = 'corrupted message' # Change the message

def send_digest(digest, digest_integrity = True):
    global DIGEST
    if digest_integrity:
        DIGEST = digest
    else:
        DIGEST = hmac.digest(key='secret'.encode(), msg='corrupted message'.encode(), digest=hashlib.sha256)

def get_message():
    return MESSAGE

def get_digest():
    return DIGEST

def send_message_digest(msg, digest, msg_integrity = True, digest_integrity = True):
    send_message(msg, msg_integrity)
    send_digest(digest, digest_integrity)


def get_message_digest():
    return get_message(), get_digest()