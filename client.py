import requests
import sys

from ecdsa import SigningKey, NIST256p
'''
In this script we first fetch ecdsa key from an api and pass it on to the api to verify it
'''
if __name__ == '__main__':
    if len(sys.argv) !=4 :
        print ('Usage python script_name val1 val2 op')
        sys.exit(1)
    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])
    op = sys.argv[3]
    url_1 = 'http://localhost:5000/get_api_key'
    response = requests.get(url_1)
    ecdsa_key = bytes.fromhex(response.text)
 
    sk = SigningKey.from_string(ecdsa_key,curve = NIST256p) 
    url_2 = 'http://localhost:5000/verify_api_key' # call the 2nd api for verification
    body = {'data':{'v1':int(val1),'v2':int(val2),'op':op}}
    str_data = str(body['data'])
    bytes_data = str.encode(str_data)
    signature = sk.sign(bytes_data) # we sign the data and send it to the server
    body['signature'] = signature.hex()

    r = requests.post(url_2,json = body)
    print(r.text)