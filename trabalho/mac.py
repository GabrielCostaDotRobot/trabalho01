# Autenticação de Mensagens
import hmac

chave = b"ciberseguranca eh o melhor curso"
mensagem = input("(HMAC) > ")
codigo = hmac.HMAC(chave, mensagem.encode(), "md5")

print(codigo.hexdigest())