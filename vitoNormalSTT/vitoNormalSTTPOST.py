import json
import requests
import vitoToken

def postSTT(voice_filepath):
    config = {
      "diarization": {
        "use_ars": False,
        "use_verification": False
      },
      "use_multi_channel": False,
      "use_disfluency_filter": True,
      "use_profanity_filter": True,
      "paragraph_splitter": {
      "min": 3,
      "max": 5
      },
    }
    resp = requests.post(
        'https://openapi.vito.ai/v1/transcribe',
        headers={'Authorization': 'bearer ' + vitoToken.vitoToken()},
        data={'config': json.dumps(config)},
        files={'file': open(voice_filepath, 'rb')}
    )
    resp.raise_for_status()
    transcribe_id = resp.json()
    print(transcribe_id)

    return transcribe_id
