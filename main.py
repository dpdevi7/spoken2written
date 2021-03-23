
import sys
from spoken2written import Spoken2Written


print("Enter/Paste your content. Ctrl-D to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)


sentence = " ".join(contents)

s2w = Spoken2Written()
print(s2w.convert(sentence))