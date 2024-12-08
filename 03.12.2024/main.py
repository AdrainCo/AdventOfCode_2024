import re

regex = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
numbers_re = re.compile(r"[0-9]{1,3}")
do_re = re.compile(r'do\([^\)]*\).*?don\'t\(\)')

def init():
    with open("input.txt", "r") as f:
        file = f.read().replace('\n', '')
    data = []
    
    do_matches = re.findall(do_re,file)
    for do_match in do_matches:
        mul_matches = re.findall(regex, do_match)
        for mul_match in mul_matches:
            numbers = re.findall(numbers_re,str(mul_match))
            data.append(numbers)
    print(data)
    return data


def first_task():
    data = init()
    result = 0
    for numbers in data:
        equasion = int(numbers[0]) * int(numbers[1])
        result += equasion
    print(result)

def second_task():
    data = init()
    result = 0
    for numbers in data:
        equasion = int(numbers[0]) * int(numbers[1])
        result += equasion
    print(result)

if __name__ == "__main__":
     second_task()