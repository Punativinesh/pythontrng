name=input("enter name")
y=int(input("enter age"))
def yearat100():
    from datetime import datetime
    t = datetime.now()
    year = t.year
    age = year - y
    year = age + 100
    print("the year at which your age is 1oo", year)
yearat100();