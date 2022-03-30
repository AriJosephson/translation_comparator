import requests
from json import load

with open('modular-seeker-345618-4d1b6f1ea15e.json') as json_file:
    file_data = load(json_file)
    almost = file_data['private_key'].strip('-----BEGIN PRIVATE KEY-----\n')
    my_key = almost.strip('\n-----END PRIVATE KEY-----')

print(my_key)

response = requests.post('https://translation.googleapis.com/language/translate/v2', data = {'q':'test',
                                                                                                   'target':'es',
                                                                                                   'format':'text',
                                                                                                   'key':my_key})

print(response)