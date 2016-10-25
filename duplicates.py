import os


def get_files_duplicates(path):
    duplicates_dict = {}
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            if (file_name, file_size) not in duplicates_dict:
                duplicates_dict[(file_name, file_size)] = [file_path]
            else:
                duplicates_dict[(file_name, file_size)].append(file_path)
    return duplicates_dict


def delete_duplicates(duplicates_dict):
    for duplicates in duplicates_dict.values():
        if len(duplicates) > 1:
            for duplicate in duplicates[1:]:
                os.remove(duplicate)
                print(duplicate, 'successfully removed.')


def print_duplicates(duplicates_dict):
    i = 0
    for one_file in duplicates_dict:
        file_name = one_file[0]
        duplicates = duplicates_dict[one_file]
        if len(duplicates) > 1:
            i += 1
            print('%s) File with name "%s" located here: %s\nAnd has duplicates:' % (i, file_name, duplicates[0]))
            for j, duplicate in enumerate(duplicates[1:]):
                print('%s.%s) %s' % (i, j+1, duplicate))


if __name__ == '__main__':
    path = input('Enter path to check duplicates_dict:\n')
    duplicate_dict = get_files_duplicates(path)
    if duplicate_dict:
        print_duplicates(duplicate_dict)
        remove_btn = input('Enter "Yes" to remove duplicates: ').lower()
        if remove_btn == 'yes':
            delete_duplicates(duplicate_dict)
    else:
        print('Duplicates not found.')
