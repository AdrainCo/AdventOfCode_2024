def init():
    f = open("input.txt", "r")
    data = [line.split() for line in f.readlines()]
    for x in range(len(data)):
        for y in range(len(data[x])):
              data[x][y] = int(data[x][y])
    return data

def first_task():
    data = init()
    safe_reports = 0
    for x in range(len(data)):
        isReportSafe = False
        type = ""
        if data[x][0] > data[x][1]:
                type = "decreasing"
        elif data[x][0] < data[x][1]:
                type = "increasing"
        else:
             continue
        
        for y in range(len(data[x])-1):
            if type == "decreasing":
                if(data[x][y] - data[x][y+1] <= 3 and data[x][y] - data[x][y+1] > 0):
                     isReportSafe = True
                else:
                    isReportSafe = False
                    break
            elif type == "increasing":
                if(data[x][y+1] - data[x][y] <= 3 and data[x][y+1] - data[x][y] > 0):
                     isReportSafe = True
                else:
                    isReportSafe = False
                    break
            else:
                    isReportSafe = False
                    break

        if isReportSafe:
            safe_reports += 1
    print(safe_reports)

def check_with_changes(report):
    for x in range(len(report)):
        tmp_report = report.copy()
        tmp_report.remove(tmp_report[x])
        if tmp_report[0] > tmp_report[1]:
            type = "decreasing"
        elif tmp_report[0] < tmp_report[1]:
            type = "increasing"
        else:
            type = ""
        for y in range(len(tmp_report)-1):
            if type == "decreasing":
                if(tmp_report[y] - tmp_report[y+1] <= 3 and tmp_report[y] - tmp_report[y+1] > 0):
                    safety = True
                else:
                    safety = False
                    break
            elif type == "increasing":
                if(tmp_report[y+1] - tmp_report[y] <= 3 and tmp_report[y+1] - tmp_report[y] > 0):
                    safety = True
                else:
                    safety = False
                    break
            else:
                safety = False
                break
        if safety:
            return True

def second_task():
    data = init()
    safe_reports = 0
    for x in range(len(data)):
        isReportSafe = False
        type = ""
        if data[x][0] > data[x][1]:
                type = "decreasing"
        elif data[x][0] < data[x][1]:
                type = "increasing"
        else:
             type = ""
        
        for y in range(len(data[x])-1):
            if type == "decreasing":
                if(data[x][y] - data[x][y+1] <= 3 and data[x][y] - data[x][y+1] > 0):
                     isReportSafe = True
                else:
                    isReportSafe = False
                    break
            elif type == "increasing":
                if(data[x][y+1] - data[x][y] <= 3 and data[x][y+1] - data[x][y] > 0):
                     isReportSafe = True
                else:
                    isReportSafe = False
                    break
            else:
                    isReportSafe = False
                    break

        if not isReportSafe:
            isReportSafe = check_with_changes(data[x])

        if isReportSafe:
            safe_reports += 1
    print(safe_reports)

"""
def check_report_safe(report,type):
    safety = False
    for x in range(len(report)-1):
        if type == "decreasing":
            if(report[x] - report[x+1] <= 3 and report[x] - report[x+1] > 0):
                safety = True
            else:
                safety = False
                break
        elif type == "increasing":
            if(report[x+1] - report[x] <= 3 and report[x+1] - report[x] > 0):
                safety = True
            else:
                safety = False
        else:
            safety = False
            break
    return safety

def second_task():
    data = init()
    safe_reports = 0
    for x in range(len(data)):
        type = ""
        if data[x][0] > data[x][1]:
            type = "decreasing"
        elif data[x][0] < data[x][1]:
            type = "increasing"
        else:
            type = ""
        isReportSafe = check_report_safe(data[x],type)

        if not isReportSafe:
            isReportSafe = check_with_changes(data[x])     

        if isReportSafe:
            safe_reports += 1

    print(safe_reports)
"""

if __name__ == "__main__":
     first_task()
     second_task()