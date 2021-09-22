def main():
    try:
        f = open("students.txt", "r")
    except(FileNotFoundError):
        print("No file 'students.txt' found.")
    prompt()


table = {}
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
        table.append(tuple(line.split(",")))


def getStudents(table, last_name, bus_route):
    for tup in table:
        if tup[STUDENT_LAST].upper() == last_name.upper() and tup[BUS] == bus_route:
            print(tup[STUDENT_LAST], tup[STUDENT_FIRST], tup[BUS])

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


if __name__ == '__main__':
    main()
