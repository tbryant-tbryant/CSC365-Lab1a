def main():
    try:
        f = open("students.txt", "r")
    except(FileNotFoundError):
        print("No file 'students.txt' found.")
    tableset = formatData(f)
    initiatePrompt(tableset)


STUDENT_LAST = 0  # STRING
STUDENT_FIRST = 1  # STRING
GRADE = 2  # INT
CLASSROOM = 3  # INT
BUS = 4  # INT
GPA = 5  # FLOAT
TEACHER_LAST = 6  # STRING
TEACHER_FIRST = 7  # STRING


def formatData(file):
    tableset = set([])
    for line in file.readlines():
        tableset.add(tuple([item.strip() for item in line.split(",")]))
    return tableset


def parseInput(request, tableset):
    pair = tuple([item.strip() for item in request.split(":")])
    if len(pair) > 1:
        if pair[0] == "Student" or pair[0] == "S":
            studentHelper([item.strip() for item in pair[1].split(" ")], tableset)
        if pair[0] == "Teacher" or pair[0] == "T":
            teacher(tableset, pair[1])
        if pair[0] == "Bus" or pair[0] == "B":
            bus(tableset, int(pair[1]))
        if pair[0] == "Grade" or pair[0] == "G":
            gradeHelper([item.strip() for item in pair[1].split(" ")], tableset)
        if pair[0] == "Average" or pair[0] == "A":
            average(tableset, int(pair[1]))


def studentHelper(tup, tableset):
    if len(tup) == 1:
        student(tableset, tup[0])
    elif len(tup) == 2:
        student_bus(tableset, tup[0], int(tup[1]))


def gradeHelper(tup, tableset):
    if len(tup) == 2:
        if tup[1] == "H" or tup[1] == "High":
            grade_high(tableset, int(tup[0]))
        elif tup[1] == "L" or tup[1] == "Low":
            grade_low(tableset, int(tup[0]))


def initiatePrompt(tableset):
    req = prompt()
    while (req != "I" and req != "Info" and
           req != "Q" and req != "Quit" and
           req[:3] != "A: " and req[:9] != "Average: " and
           req[:3] != "G: " and req[:7] != "Grade: " and
           req[:3] != "B: " and req[:5] != "Bus: " and
           req[:3] != "T: " and req[:9] != "Teacher: " and
           req[:3] != "S: " and req[:9] != "Student: "):
        req = prompt()
    if req == "Q" or req == "Quit":
        quit()
    elif req == "I" or req == "Info":
        info(tableset)
    parseInput(req, tableset)


def student(table, last_name):
    for tup in table:
        if tup[STUDENT_LAST].upper() == last_name.upper():
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST],
                  tup[GRADE],
                  tup[CLASSROOM],
                  tup[TEACHER_LAST],
                  tup[TEACHER_FIRST])


def student_bus(table, last_name, bus_route):
    for tup in table:
        if tup[STUDENT_LAST].upper() == last_name.upper() and int(tup[BUS]) == bus_route:
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST],
                  tup[BUS])


def teacher(table, last_name):
    for tup in table:
        if tup[TEACHER_LAST].upper() == last_name.upper():
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST])


def grade(table, last_name):
    for tup in table:
        if tup[TEACHER_LAST].upper() == last_name.upper():
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST])


def bus(table, bus_route):
    for tup in table:
        if int(tup[BUS]) == bus_route:
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST],
                  tup[GRADE],
                  tup[CLASSROOM])


def grade_high(table, grade):
    highest_gpa = 0.0
    for tup in table:
        if int(tup[GRADE]) == grade:
            if float(tup[GPA]) > highest_gpa:
                highest_gpa = float(tup[GPA])
    for tup in table:
        if int(tup[GRADE]) == grade and float(tup[GPA]) == highest_gpa:
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST],
                  tup[GPA],
                  tup[TEACHER_LAST],
                  tup[TEACHER_FIRST],
                  tup[BUS])


def grade_low(table, grade):
    lowest_gpa = 10.0
    for tup in table:
        if int(tup[GRADE]) == grade:
            if float(tup[GPA]) < lowest_gpa:
                lowest_gpa = float(tup[GPA])
    for tup in table:
        if int(tup[GRADE]) == grade and float(tup[GPA]) == lowest_gpa:
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST],
                  tup[GPA],
                  tup[TEACHER_LAST],
                  tup[TEACHER_FIRST],
                  tup[BUS])


def average(table, grade):
    total = 0.0
    num = 0
    for tup in table:
        if int(tup[GRADE]) == grade:
            total += float(tup[GPA])
            num += 1
    if num != 0:
        print(grade, total / num)


def info(table):
    for i in range(7):
        total = 0
        for tup in table:
            if int(tup[GRADE]) == i:
                total += 1
        print(str(i) + ":", str(total))


def info(table):
    for i in range(7):
        total = 0
        for tup in table:
            if int(tup[GRADE]) == i:
                total += 1
        print(str(i) + ":", str(total))


def prompt():
    print('''Commands:
        S[tudent]: <lastname> [B[us]]
        T[eacher]: <lastname>
        B[us]: <number>
        G[rade]: <number> [H[igh] | L[ow]]
        A[verage]: <number>
        I[nfo]
        Q[uit]''')
    request = input("Request: ")
    return request


if __name__ == '__main__':
    main()
