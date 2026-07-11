print("-------------        TO DO LIST       ------------")
print("Create Your Task")
last=[]
print("Enter your task or Done if You are done: ")
def create(last):
    while True: 
        a=(input("enter your task: "))
        if a=="done":
            return
        last.append(a)
        b=(input("enter your task: "))
        if b=="done":
            return
        last.append(b)
create(last)
print("YOUR TASKS ARE:")

for i in last:
    print("-",i)


def update(last):
    for index,task in enumerate(last):
        
        c=(input(f"{task} done or not done(d/n): "))
        if c== "d":
            last[index]=last[index]+"✅"
        else:
                pass
update(last)
print("--------------Your Tasks condition:--------------")

for i in last:
    print("-",i)

def delete(last):
    for index,task in enumerate(last[:]):
        x=input(f"do you want to delete this (y/n)\n{task}: ")
        if x=="y":
            last.remove(task)
        else:
            pass

delete(last)
print("--------YOUR FINAL TASK:-----------")
for i in last:
    print("*",i)

# 7/11/2026