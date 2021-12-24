students_file = open("students.txt", "r")


lines = students_file.readlines()
print(type(lines))


n = 5
first_lines = lines[:n]
last_lines = lines[-n:]

x = 'Bouras Amdjed'
print(x in lines)


#getting ASCII code between 97 and 123 will give us the alphabet
alphabet = [chr(x).capitalize() for x in range(97, 123)]


for letter in alphabet:
  f = open(letter+'.txt', "x")
  f.close()
