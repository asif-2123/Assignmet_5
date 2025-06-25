marks={'Mike':'80','George':'90','Jack':'64','Oggy':'79'}
name=input("Enter the student's name:")
if name in marks:
    print(name+('\'s marks:')+marks[name])
else:
    print('Student not found.')