import json
import sys


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file {file_path}: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error writing JSON to file {file_path}: {e}")
        sys.exit(1)


def create_value_map(values):
    return {item['id']: item['value'] for item in values['values']}


def fill_values(test_structure, value_map):
    if 'id' in test_structure and test_structure['id'] in value_map:
        test_structure['value'] = value_map[test_structure['id']]
    if 'values' in test_structure:
        for subtest in test_structure['values']:
            fill_values(subtest, value_map)


def main(values_file, tests_file, report_file):
    values = load_json(values_file)
    tests = load_json(tests_file)

    value_map = create_value_map(values)

    for test in tests['tests']:
        fill_values(test, value_map)

    save_json(tests, report_file)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)
