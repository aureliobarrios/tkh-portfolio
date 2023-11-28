
def get_todo():
    with open("10_24/code_along/data/todo.txt") as f:
        lines = f.readlines()

        for row in lines:
            print(row)


print("youve ran todo.py")

if __name__ == "__main__":
    print("you've now ran the dtime module")