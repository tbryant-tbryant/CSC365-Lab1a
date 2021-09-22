def main():
    try:
        f = open("students.txt", "r")
    except(FileNotFoundError):
        print("No file 'students.txt' found.")
    initiatePrompt()

def initiatePrompt():
    req = prompt()
    while (req != "I" and req != "Info" and
           req != "Q" and req != "Quit" and
           req != "A" and req[:8] != "Average" and
           req != "G" and req[:6] != "Grade" and
           req != "B" and req[:4] != "Bus" and
           req != "T" and req[:8] != "Teacher" and
           req != "S" and req[:8] != "Student"):
        req = prompt()

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
