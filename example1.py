import hashlib
import hmac
from mac import send_message_digest, get_message_digest

SECRET_KEY = 'secret'


if __name__=='__main__':
    # Alice is encoding a message with HMAC
    message = 'Hash and MACs'
    alice_digest = hmac.digest(key=SECRET_KEY.encode(), msg=message.encode(), digest=hashlib.sha256)
    print(f'MAC generated by Alice : {alice_digest}')

    # Alice send the message to Bob
    send_message_digest(message, alice_digest)

    # Bob received the message from Alice
    message_received, digest_received = get_message_digest()

    print(f'Message received : {message_received}')
    print(f'Digest received : {digest_received}')

    # Bob check the message integrity
    bob_digest = hmac.digest(key=SECRET_KEY.encode(), msg=message_received.encode(), digest=hashlib.sha256)

    # Bob compare the 2 digest
    message_valid = hmac.compare_digest(digest_received, bob_digest)

    print(f'Message is integre : {message_valid}')


