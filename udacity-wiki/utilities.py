import difflib

def added_removed(a, b):
    output = []
    for i in enumerate(difflib.ndiff(a, b)):
        output.append(i)
    added = ''
    removed = ''
    for i in output:
        if i[1][0] == '-':
            removed += i[1][2:]
        if i[1][0] == '+':
            added += i[1][2:]

    return (added, removed)

print(added_removed('я вас любил', 'вас не любил'))