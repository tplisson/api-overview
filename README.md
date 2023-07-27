# REST API

Representational State Transfer (REST) Application Programming Interface (API)

API operations
- GET
- POST
- PUT
- PATCH
- DELETE

## API Tools  

### cURL  

```console
curl https://catfact.ninja/fact

{"fact":"Neutering a cat extends its life span by two or three years.","length":60}

curl -X PUT <URL>
     -d "PUT request data"
```

```console
curl -X POST https://reqbin.com/echo/post/json \
   -H 'Content-Type: application/json' \
   -d '{"login":"my_login","password":"my_password"}'

{
    "success": "true"
}
```

Output in [JSON](https://www.w3schools.com/js/js_json_intro.asp)


### POSTMan  


## Google Maps API

curl -L -X GET 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=$GCP_KEY_ID'

```python
import requests

YOUR_API_KEY = os.environ["GCP_KEY_ID"]

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=YOUR_API_KEY"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```