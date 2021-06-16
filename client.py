import requests
import sys
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
    url_2 = 'http://localhost:5000/verify_api_key'
    body = {'data':{'v1':val1,'v2':val2,'op':op,},'signature': response.text}
    r = requests.post(url_2,json = body)
    print(r.text)
