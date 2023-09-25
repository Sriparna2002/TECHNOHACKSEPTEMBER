
import requests

url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params = {
    "from " : input("Enter from currency code : ").upper(),
    "to" : input("Enter to currency code : ").upper(),
    "amount" : float(input("Enter amount : "))
})
data = response.json()['result']

rounded_data = round(data, 2)

print(f'Converted Amount: {rounded_data}')

