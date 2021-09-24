def main():
    try:
        f = open("students.txt", "r")
    except(FileNotFoundError):
        print("No file 'students.txt' found.")
    formatData(f)
    initiatePrompt()

table = set([])
STUDENT_LAST = 0  # STRING
STUDENT_FIRST = 1  # STRING
GRADE = 2  # INT
CLASSROOM = 3  # INT
BUS = 4  # INT
GPA = 5  # FLOAT
TEACHER_LAST = 6  # STRING
TEACHER_FIRST = 7  # STRING

def formatData(file):
    for line in file.readlines():
        table.add(tuple([item.strip() for item in line.split(",")]))

def parseInput(request):
    pair = request.split(":")
    if len(pair) > 1:
       if pair[0] == "Student" or pair[0] == "S":
           #studentHelper(pair)
           a = 0
       if pair[0] == "Teacher" or pair[0] == "T":
           teacher(table, pair[1])
       if pair[0] == "Bus" or pair[0] == "B":
           bus(table, pair[1])
       if pair[0] == "Grade" or pair[0] == "G":
           #gradeHelper(pair)
           a = 0
       if pair[0] == "Average" or pair[0] == "A":
           average(table, pair[1])

def studentHelper(tup):
    a = 0

def initiatePrompt():
    req = prompt()
    while (req != "I" and req != "Info" and
           req != "Q" and req != "Quit" and
           req[:2] == "A:" and req[:9] != "Average:" and
           req[:2] == "G:" and req[:7] != "Grade:" and
           req[:2] == "B:" and req[:5] != "Bus:" and
           req[:2] == "T:" and req[:9] != "Teacher:" and
           req[:2] == "S:" and req[:9] != "Student:"):
        req = prompt()
    if (req == "Q" or req == "Quit"):
        quit()
    elif (req == "I" or req == "Info"):
        info(table)
    #print(req + '\n')
    parseInput(req)

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
        if tup[STUDENT_LAST].upper() == last_name.upper() and tup[BUS] == bus_route:
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
        if tup[BUS] == bus_route:
            print(tup[STUDENT_LAST],
                  tup[STUDENT_FIRST],
                  tup[GRADE],
                  tup[CLASSROOM])

def grade_high(table, grade):
    highest = ()
    highest_gpa = 0.0
    for tup in table:
        if tup[GRADE] == grade:
            if tup[GPA] > highest_gpa:
                highest_gpa = tup[GPA]
    for tup in table:
        if tup[GRADE] == grade and tup[GPA] == highest_gpa:
            print(highest[STUDENT_LAST],
                  highest[STUDENT_FIRST],
                  highest[GPA],
                  highest[TEACHER_LAST],
                  highest[TEACHER_FIRST],
                  highest[BUS])

def grade_low(table, grade):
    lowest = ()
    lowest_gpa = 10.0
    for tup in table:
        if tup[GRADE] == grade:
            if tup[GPA] < lowest_gpa:
                lowest_gpa = tup[GPA]
    for tup in table:
        if tup[GRADE] == grade and tup[GPA] == lowest_gpa:
            print(lowest[STUDENT_LAST],
                  lowest[STUDENT_FIRST],
                  lowest[GPA],
                  lowest[TEACHER_LAST],
                  lowest[TEACHER_FIRST],
                  lowest[BUS])

def average(table, grade):
    total = 0.0
    num = 0
    for tup in table:
        if tup[GRADE] == grade:
            total += tup[GPA]
            num += 1
    if num != 0:
        print(grade, total / num)

def info(table):
    for i in range(7):
        total = 0
        for tup in table:
            #print("Makes it here too\n")
            if tup[GRADE] == str(i):
                #print("Makes it here\n")
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
