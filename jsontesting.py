import json
import os

source_dir = os.path.dirname('files/')
full_path=os.path.join(source_dir, 'first.json')
file= open(full_path,'r')
contents=file.read()
file.close()
data=json.loads(contents)
print(str(data) + '\n')

jString=json.dumps(data, indent=2, sort_keys=True)
print(jString)