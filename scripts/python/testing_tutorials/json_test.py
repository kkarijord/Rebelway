import json as j

python_dict = {
    'name': 'Houdini',
    'version': 20.5,
    'user': 'Kristian',
    'license': 'Core',
    'auto_renew': False,
    'address': {
        'street': 'Kristine Bonnevies vei 20',
        'city': 'Oslo',
        'postCode': 12345
    }

}

#create json_file
# with open("data.json","w") as file:
#     j.dump(python_dict, file,indent=4,sort_keys=True)


# json_data = '{"products":["apple","banana","cherry"], "sell":false}'

# with open("data.json","r+") as file:
#     data = j.load(file)

#     data["file_format"]= "hip"
#     del data["version"]

#     file.seek(0)
#     file.truncate()
#     j.dump(data,file,indent=4,sort_keys=True)