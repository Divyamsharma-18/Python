#  Strings are immutable i.e. can't be changed - i.e. can't replace a with b


name = "Divit"

nameshort = name[0:3]       # Starts from 0 then goes to 2 i.e. 0,1,2 and 3 will be excluded, it's like telling it that don't count anything starting from 3rd Index

print(nameshort)

char1 = name[4]

print(char1)


# negative slicing

print(name[0:3])

print(name[-4:-1])      # arr i.e. in -ve value goes like -4, -3, -2, -1, 0

print(name[1:4])        # arr cause yk why

print(name[1:])     # ivit cause starts from 1 index and goes till the last

print(name[:4])     # Divi cause takes 0 to 3 and yk from 4 it excludes everything 