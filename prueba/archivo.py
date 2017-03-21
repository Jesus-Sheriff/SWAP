import json



data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data)
data = json.loads(json_str)
with open('archivo.json', 'w') as f: #si no existe el archivo lo crea
     json.dump(data, f)
print(' ----')
with open('archivo.json', 'r') as json_data:
    d = json.load(json_data)
    print(d)