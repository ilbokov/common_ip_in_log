import os, re
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

ip_addresses = {}

with open(str(os.environ.get('FILE_NAME')), encoding=str(os.environ.get('ENCODING'))) as file:
    for line in file:
        if (os.getenv('HOST') in line) and (os.getenv('TYPE') in line):
            try:
                ip_addresses[re.search(r'[0-9]+(?:\.[0-9]+){3}', line).group()] += 1
            except KeyError:
                ip_addresses[re.search(r'[0-9]+(?:\.[0-9]+){3}', line).group()] = 1

sorted_adresses = sorted(ip_addresses.items(), key=lambda x: x[1])[::-1]

for k, v in sorted_adresses[:10]:
     print(f'{k} - {v}')