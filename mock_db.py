from datetime import datetime


mock_db = [
    {
        'id': 'qwerty1',
        'title': 'First todo',
        'description': 'It is the first "todo"',
        'deadline': datetime.strptime('1.07.2023', '%d.%m.%Y').timestamp(),  # 1688148000.0
        'is_close': True
    },
    {
        'id': 'qwerty2',
        'title': 'Second todo',
        'description': 'It is the second "todo"',
        'deadline': datetime.strptime('2.07.2023', '%d.%m.%Y').timestamp(),  # 1688234400.0
        'is_close': True
    },
    {
        'id': 'qwerty3',
        'title': 'Third todo',
        'description': 'It is the third "todo"',
        'deadline': datetime.strptime('3.07.2023', '%d.%m.%Y').timestamp(),  # 1688320800.0
        'is_close': True
    }
]


if __name__ == '__main__':
    # print(datetime.strptime('1.07.2023', '%d.%m.%Y').timestamp())
    # print(datetime.strptime('2.07.2023', '%d.%m.%Y').timestamp())
    # print(datetime.strptime('3.07.2023', '%d.%m.%Y').timestamp())
    pass
