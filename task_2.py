'''
2. Create a python method that takes a json element
as an argument, and removes that element from test_payload.json.

Please verify that the method can remove either nested or non-nested elements
(try removing "outParams" and "appdate").

Please write the modified json to a new file.
'''

import json
import copy

def remove_jsonkeys(data):
    out_data = copy.deepcopy(data)
    inner_key_to_delete = 'appdate'
    outer_key_to_delete = 'outParams'

    for outerkey in data:
        if isinstance(data[outerkey], (list, dict)):
            for innerkey in data[outerkey]:
                if innerkey == inner_key_to_delete:
                    del out_data[outerkey][innerkey]
        if outerkey == outer_key_to_delete:
            del out_data[outerkey]

    return out_data

json_file = 'test_payload.json'

with open(json_file) as f:
    data = json.load(f)
    new_data = remove_jsonkeys(data)

with open('test_payload_out.json', 'w') as f:
    json.dump(new_data, f, indent=2)

