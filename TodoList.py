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
    print("-" * 20)
    if len(todos) == 0:
        print(" ---  Empty  ---")
    else:
        for index, item in enumerate(todos):
            print(f"{index + 1}. {item['text']}")
    print("-" * 20)


def add():
    global id
    text = input("Enter todo text: ")
    newTodo = {"id": id + 1, "text": text}
    id += 1
    todos.append(newTodo)
    print("* New todo added")
    store()


def edit():
    display()
    ind = int(input("Enter the number of Todo: "))
    if 1 <= ind <= len(todos):
        text = input("Enter updated todo: ")
        todos[ind - 1]['text'] = text
    else:
        print("*** Invalid Number")


def delete():
    display()
    ind = int(input("Enter the number of Todo to delete: "))
    if 1 <= ind <= len(todos):
        deleted_todo = todos.pop(ind - 1)
        print(f"* Deleted: {deleted_todo['text']}")
        store()
    else:
        print("Invalid Number")


load()

while True:
    print("\nOptions:")
    print("1. List All Todos")
    print("2. Add New Todo")
    print("3. Edit Todo")
    print("4. Delete Todo")
    print("5. Exit")
    opt = input("Enter the option number: ")

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
    else:
        print("Invalid option. Please choose a valid option (1-5).")

print("Goodbye!")
