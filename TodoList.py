import json
todos = []
id = 0


def store():
    with open("todos.json", "w") as f:
        json.dump({"id": id, "todos": todos}, f)


def load():
    global id, todos
    try:
        with open('todos.json', 'r') as f:
            obj = json.load(f)
            id = obj['id']
            todos = obj['todos']
    except:
        with open("todos.json", "w") as f:
            json.dump({"id": 0, "todos": []}, f)


def display():
    print("-"*20)
    if len(todos) == 0:
        print(" ---  Empty  ---")
    for index, item in enumerate(todos):
        print(f"{index+1}. {item['text']}")
    print("-"*20)


def add():
    global id
    text = input("Enter todo text: ")
    newTodo = {"id": id+1, "text": text}
    id += 1
    todos.append(newTodo)
    print("* New todo added")
    store()


def edit():
    display()
    ind = int(input("Enter the number of Todo: "))
    if ind > 0 and ind <= len(todos):
        text = input("Enter todo: ")
        todos[ind-1]['text'] = text
    else:
        print("*** Invalid Number")


def delete():
    display()
    ind = int(input("Enter the number of Todo: "))
    if ind > 0 and ind <= len(todos):
        todos.pop(ind-1)
        print("* Deleted")
        store()
    else:
        print("Invalid Number")


load()
while True:
    opt = input(
        "\n1.List All Todos\n2.Add New Todo\n3.Edit Todo\n4.Delete Todo\n5.Exit\nEnter the option number:")
    if opt == '1':
        display()
    elif opt == '2':
        add()
    elif opt == '3':
        edit()
    elif opt == '4':
        delete()
    elif opt == '5':
        break
