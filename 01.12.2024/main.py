#Initialization
first_list = []
second_list = []
def init():
    f = open("input.txt", "r")

    tmp_list = [line.split() for line in f.readlines()]
    for x in range(len(tmp_list)):
        for y in range(len(tmp_list[x])):
            if y%2==0:
                second_list.append(tmp_list[x][y])
            else:
                first_list.append(tmp_list[x][y])


#first part
def first_task():
    init()
    result = 0


    for x in range(len(first_list)):
        first_value = int(min(first_list))
        second_value = int(min(second_list))
        number = max(first_value,second_value) - min(first_value,second_value)
        first_list.remove(min(first_list))
        second_list.remove(min(second_list))
        result += number

    print(result)

#second part
def second_task():
    init()

    result_1 = 0
    for x in range(len(first_list)):
        counter = 0
        for y in range(len(second_list)):
            if int(second_list[y]) == int(first_list[x]):
                counter += 1
        number = int(first_list[x])*counter
        result_1 += number

    print(result_1)

if __name__ == "__main__":
    first_task()
    second_task()