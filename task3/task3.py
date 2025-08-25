import json

with open('values.json', 'r') as f:
    values_data = json.load(f)['values']

with open('tests.json', 'r') as f:
    tests_data = json.load(f)

value_dict = {item['id']: item['value'] for item in values_data}

def fill_values(test):
    if 'id' in test:
        test['value'] = value_dict.get(test['id'], "")
    if 'values' in test:
        for subtest in test['values']:
            fill_values(subtest)

for test in tests_data['tests']:
    fill_values(test)

with open('report.json', 'w') as f:
    json.dump(tests_data, f, indent=2)