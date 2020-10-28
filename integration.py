# """open and read input.yaml  - - - done"""
# """send an api request based on the object received from input to swapi.dev  - - - done"""
# """parse the response from swapi and save data, in json format, for only the keys provided in input.yaml  - - - done"""
# """format the aggregate response object to write to a file named swapi-output.json  - - - done"""
"""dockerize the script (should be deployable to k8s via helm chart)"""

import requests
import yaml

output = []

#write a function to take in a yaml file and open it, then save it to memory
with open(r'input.yaml') as file:
    documents = yaml.full_load(file)

    #iterate through the items in the yaml
    for k, v in documents.items():
        for swapi_object in v:
            #build the request to the swapi API, normally I'd break this into its own function to allow it to be more DRY and reusable for other means, but it's not in the scope of this project
            response = requests.get(url=f"https://swapi.dev/api/{swapi_object['type']}/{swapi_object['id']}").json()

            #store each dict for the output
            list_item = {}
            
            #from the larger response json, filter to only return k/v pairs to write to the file that were requested in infoRequest from input.yaml
            for key in swapi_object['infoRequest']:
                #add key and value that has not been filtered to be a stored dict to join to the output
                list_item[key] = response[key]
            #append the larger output list with all iterated items from input.yaml
            output.append(list_item)
            print(list_item)


#create a new fiel in the dir to house my json data
create_json = open('swapi-output.json', 'x')

#write the final list of dicts or json to a .json formatted file
with open('swapi-output.json', 'r+') as output_file:
        output_file.write(f'{output}')
        print(output)