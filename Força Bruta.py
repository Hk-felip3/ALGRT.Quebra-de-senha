import itertools
import time
from zipfile import ZipFile

inicio = time.time()
def forcaBruta(file, senha_tamanho, charset):

#                      product('ABCD', repeat=2) ---> AAAA AAAB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

for senha in itertools.product(charset, repeat=senha_tamanho):
senha = ''.join(senha)
if verifica_senha(file, senha):
return senha
return None
def verifica_senha(file, senha):
try:
file.extractall(pwd=senha.encode())
return True
except Exception:
print(senha)
pass

#charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@'

charset = '0123456789' # 9139
senha_tamanho = 4
arquivo = ZipFile('testeArquivo.zip', 'r')
#PTlm8826@
senha = forcaBruta(arquivo, senha_tamanho, charset)
fim = time.time()
if senha:
print(f'Senha encontrada: {senha}')
print('tempo:', fim - inicio)
else:
print('não foi possivel encontrar a senha!')















