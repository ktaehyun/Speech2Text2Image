import requests

# 6시간마다 토큰을 갱신해야 돼서 5시간 30분에 1번 실행시켜줘야 한다.
def vitoToken():
    resp = requests.post(
        'https://openapi.vito.ai/v1/authenticate',
        data={'client_id': 'r-8-juMBoCXmc8RahkDu',
              'client_secret': 'CARYeGX3cll3Lu40lP2mcRwtin48ZuMYCls1DJhf'}
    )
    resp.raise_for_status()
    return resp.json()['access_token']


