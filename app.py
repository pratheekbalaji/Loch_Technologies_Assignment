from flask import Flask, request, abort, make_response, jsonify

from ecdsa import SigningKey, NIST256p
import json
app = Flask(__name__)
session = {}

@app.route('/get_api_key')
def get_api_key():
    sk = SigningKey.generate(curve = NIST256p) # generates signing key with base 64 encoding
    
    session['vk'] = sk.verifying_key
    sk_string = sk.to_string() # serializes signing key in the form of bytes

    return sk_string.hex() # we return the output in the form of string

@app.route('/verify_api_key',methods=['GET','POST'])
def verify_api_key():
    '''
    The module verifies the data field which is sent as a parameter using ecdsa keys, if it is verified it performs a
    basic calculator functionality involving just 2 operands
    '''
    try:
        content = request.json
        # converting json data to string form and then bytes
        str_data = str(content['data'])
        bytes_data = str.encode(str_data)
        signature = bytes.fromhex(content['signature'])
        vk = session['vk']
        
        assert vk.verify(signature,bytes_data)  # verifying the signature
        valid_operators = {'+','-','/','*','%','**','//'}
        val1 = str(content['data']['v1']) # operand1
        val2 = str(content['data']['v2']) # operand2
        op = content['data']['op']
        if op not in valid_operators:
            data = {'message':'Invalid Operator', 'code': 'FAILURE'}
            return make_response(json.loads(data), 500)
    
        expression = val1 + op + val2
        res = eval(expression)
        data = {'result': res, 'code': 'SUCCESS'}
        return make_response(data, 200)
    
    except :
        abort(400,'Signature not matched')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

