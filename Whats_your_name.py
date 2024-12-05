def hello(name):
    return f'Какое красивое имя, {name}!'

class Name:
    def __init__(self, name):
        self.name = name
if __name__ ==  "__main__":
    user_input = input('Как тебя зовут: ').strip()
    if not  user_input:
        print('Ваше имя не может быть пустым')
    else:
        person = Name(user_input)
        print(hello(person.name))

