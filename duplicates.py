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
    duplicates = filter(lambda x: len(x) > 1, duplicates_dict.values())
    for duplicate in duplicates:
        for one_file in duplicate[1:]:
            os.remove(one_file)
            print_deleted_duplicate(one_file)


def print_deleted_duplicate(file_path):
    print('%s was removed.' % file_path)


def print_duplicates(duplicates_dict):
    duplicates = filter(lambda x: len(x) > 1, duplicates_dict.values())
    for duplicate in duplicates:
        print('\nBasic file located here: %s\nAnd has duplicates:' % duplicate[0])
        for i, current_duplicate in enumerate(duplicate[1:]):
            print('\t%s) %s' % (i+1,current_duplicate))


if __name__ == '__main__':
    path = input('Enter path to check duplicates:\n')
    duplicate_dict = get_files_duplicates(path)
    if list(filter(lambda x: len(x) > 1, duplicate_dict.values())):
        print_duplicates(duplicate_dict)
        remove_btn = input('Enter "Yes" to remove duplicates: ').lower()
        if remove_btn == 'yes':
            delete_duplicates(duplicate_dict)
    else:
        print('Duplicates not found.')
