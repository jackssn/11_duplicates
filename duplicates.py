import os


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
            duplicate_list = list(file_list[file].values())
            copies = []
            for i, duplicate in enumerate(duplicate_list):
                size_base = duplicate[0]
                for d in duplicate_list[i+1:]:
                    if d[0] == size_base and d[1] not in copies:
                        copies.append(d[1])
            if copies:
                duplicates.append({file: {'base': file_list[file][0][1], 'copies': copies}})
    if duplicates:
        return duplicates
    return None


def delete_duplicates(duplicate_list):
    for duplicate_name in duplicate_list:
        files = duplicate_name.values()
        for file in files:
            copies = file['copies']
            for copy in copies:
                os.remove(copy)
                print(copy, 'successfully removed.')


def print_duplicates(duplicates):
    for duplicate in duplicates:
        file_name = list(duplicate.keys())[0]
        file_paths = list(duplicate.values())[0]
        print('File "%s" located at "%s" and has copies:' % (file_name, file_paths['base']))
        for copy in file_paths['copies']:
            print('-> "%s"' % copy)


if __name__ == '__main__':
    path = input('Enter path to check duplicates:\n')
    duplicate_list = get_files_duplicates(path)
    if duplicate_list:
        print_duplicates(duplicate_list)
        remove_btn = input('Enter "Yes" to remove all duplicates:\n').lower()
        if remove_btn == 'yes':
            delete_duplicates(duplicate_list)
    else:
        print('Duplicates not found.')
