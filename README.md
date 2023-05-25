# A simple Python library for the Musixmatch Web API
### Installation
```
pip install mxmapi
```

### Quick Start

How to get track by spotify track id:

To get started, install mxmapi and create an app on https://developer.musixmatch.com/ .Use your API KEY

```Python
from mxmapi import Musixmatch

# Instantiate a Musixmatch object
musixmatch = Musixmatch(API_key='your_api_key')

# Call the get_track method
result = musixmatch.track_get(track_spotify_id="6kwAbEjseqBob48jCus7Sz")
track =result["message"]["body"]["track"]
```