import hashlib as h

msg = input('> ').encode()

hash_code = h.md5(msg).hexdigest()
print(hash_code)