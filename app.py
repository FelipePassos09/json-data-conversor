import requests as rq
import json
import zipfile


filename_json = './dadosFormatado.json'

zip = zipfile.ZipFile('./zipoutput.zip', 'w', zipfile.ZIP_DEFLATED)
zip.write(filename_json)
zip.close()

#Requisition compile:

organizationId = '6eb21dea-c3cd-4171-b201-19c811faf476'
processId = '62c861a5bf0ddb0939fdd509'
urlUpflux = 'https://ingestor-service-v3.upflux.me'
servicoUp = f'/LoadProcess/zip/{processId}/oid/{organizationId}'
accessKey = 'IKS1loj8Z6V2Mfl+vI/xf9LAKV1RVrUOIUQ5svwal0uIf455rVA5rBdfaS63syRCeOMOVjU1UJw3sI8ocSnq7XsDBQgxzbOlBiT6IhGDEHa/ioMtZMEyRML2+H/yIgeP3JnSoCsKy6sP7Nby+upyUOyKFluaUCSOJzTD++9G6MLsdqInY3sxSwG+z0/XOZTxiYHiYDYpwypP4NiXFqtbiIU1NmcaTVvf8bMmBVOYa5IQfR8tevV2RCCopZoleURn9t8yGqhjvzzYCBRggjjz29gXOit2p3759IRKnWTGdoe+wE/NJeD50qHdZzJEdWlD8MutPbkitM2sdtU2lfNiQgTrdKOs8gsVV+fVjNg1l259Xt2yKtygl4ChiV3wsPf5+1GiD/H9V8DbbGC49Gt9jfpf0mreFEm9ZhvitL5xRO8AoM1J9wC1Ub1E1YjVmNMmiRE1K31sUqkbPRS9DL7cmLuPrDqSLVrCoavjiWocmLtR+Rwg67i56AHcf5EQbBE02It9gdnZPc3Nd9qW9YPkDohBc37CMIq5viZ+ZjgSmTpa2aRS5bIKYL1ABbI0QYzHqg0OpsuiYzbg30KfMqV0d0fl9SF/N7hfeXfTe+ACWMZZDtJs01U59N2z08VRujjyR3sDwY5dil6iWJwAofXRg7sA7VeOxEGVqc9Wf/k9vl+ZwkmfwLO0BxHSgiZRpkj0mY0kFtt+uAzbGDVXchUfvSHmISl9OoOleldlGfJnISwuo9ybRghqmA1JVRvZVpLOpZYo0WcUYFMnZeyvPyMGCEbwGtmk4E/huxnyQ33tZNXrj8Ypxcj8y7zDu30Mux4E7BD7CM8XMtHpE6DquAp8sBWta1eK6Z7cDg7ulHYqpRQlDaYoUu+pfKIVWNcspgMPlsLIQzSlOTC1BEEUj07fCb+0pv+xPEfXGFwMrxZWEq6jVEKkQ9I0WHExUEU58zrxZMtPDaKTukZ+ido0W3wYGiNrUIOA6XRYng5YCR2RcefgDu5hrssivPzQzWIbjm3x'



# requicicao = rq.post(urlUpflux+servicoUp, data = str(body))

files = [('eventLog',('file', open('./eventlog1.zip', 'rb'), 
         'application/octet-stream'))
         ]

headers = {
    'groupId': organizationId,
    'Accept': 'application/json',
    'Authorization': accessKey
}

requisicao = rq.request('POST', url = urlUpflux+servicoUp, headers = headers, files = files)
print(requisicao.text)

print('done')