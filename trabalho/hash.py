import hashlib

mensagem = input("> ")
codigo_md5 = hashlib.md5(mensagem.encode())
codigo_md5 = codigo_md5.hexdigest()
print(codigo_md5)