import os
from pprint import pprint


def get_files_duplicates(path):
    file_list = {}
    duplicates = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            if file_name not in file_list:
                file_list[file_name] = {0: (file_size, file_path)}
            else:
                duplicate_num = len(file_list[file_name])
                file_list[file_name][duplicate_num] = (file_size, file_path)

    for file in file_list:
        if len(file_list[file]) > 1:
            duplicate_list = [x for x in file_list[file].values()]
            copies = []
            for i, duplicate in enumerate(duplicate_list):
                size_base = duplicate[0]
                for d in duplicate_list[i+1:]:
                    if d[0] == size_base and d[1] not in copies:
                        copies.append(d[1])
            duplicates.append({file: {'base': file_list[file][0][1], 'copies': copies}})
    if not duplicates:
        return 'Duplicates not found'
    return duplicates


def delete_duplicates(file_names):
    for file_name in file_names:
        duplicates = [x for x in file_name.values()]
        for duplicate in duplicates:
            copies = duplicate['copies']
            for copy in copies:
                print(copy, 'removed.')
                os.remove(copy)


if __name__ == '__main__':
    path = input('Enter path to check duplicates:\n')
    duplicates = get_files_duplicates(path)
    pprint(duplicates)
    remove_btn = input("Remove duplicates? yes / no\n").lower()
    if remove_btn == 'yes':
        delete_duplicates(duplicates)
        print('Success.')
