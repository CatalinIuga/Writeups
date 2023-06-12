# Unmix The Flag

## Challenge Description

Try to find the flag! :)
Wait... Here's the encryption:
`⠱⠁ ⠹⠣ ⠱⠹ ⠱⠁ ⠹⠣ ⠹⠳ ⠱⠁ ⠹⠣ ⠹⠪ ⠱⠁ ⠹⠣ ⠱⠩ ⠹⠣ ⠱⠩ ⠹⠱ ⠻⠁ ⠫⠩ ⠫⠡ ⠻⠻ ⠹⠣ ⠱⠩ ⠹⠱ ⠻⠁ ⠻⠪ ⠻⠁ ⠻⠱ ⠫⠡ ⠻⠻ ⠫⠡ ⠫⠩`
Make sure to enclose the message inside the TUCTF{}. Have Fun!!

## Attached Files

- flag_unmixer.py

```python
import string

upperFlag = string.ascii_uppercase[:26]
lowerFlag = string.ascii_lowercase[:26]
MIN_LETTER = ord("a")
MIN_CAPLETTER = ord("A")

def mix(oneLetter,num):

    if(oneLetter.isupper()):
        word = ord(oneLetter)-MIN_CAPLETTER
        shift = ord(num)-MIN_CAPLETTER
        return upperFlag[(word + shift)%len(upperFlag)]
    if(oneLetter.islower()):
        word = ord(oneLetter)-MIN_LETTER
        shift = ord(num)-MIN_LETTER
        return lowerFlag[(word + shift)%len(upperFlag)]

def puzzled(puzzle):
    toSolveOne = ""
    for letter in puzzle:

        if (letter.isupper()):
            binary ="{0:015b}".format(ord(letter))

            toSolveOne += upperFlag[int(binary[:5],2)]
            toSolveOne += upperFlag[int(binary[5:10],2)]
            toSolveOne += upperFlag[int(binary[10:],2)]

        elif(letter.islower()):
            six = "{0:02x}".format(ord(letter))
            toSolveOne += lowerFlag[int(six[:1],16)]
            toSolveOne += lowerFlag[int(six[1:],16)]
        elif(letter == "_"):
            toSolveOne += "CTF"
    return toSolveOne


flag = "Figure it Out! :)"
numShift = "k"
mixed = ""

assert all([x in lowerFlag for x in numShift])
assert len(numShift) == 1

encoding = puzzled(flag)
print(encoding)
for count, alpha in enumerate(encoding):
    mixed += mix(alpha, numShift)

print(mixed)
```

## Solution

I took a bit of a brute force approach. After running the Braille translator we get `5a42545a42485a42495a42534253457a6361774253457a797a7561776163`, and running that intro a from hex convertor we get `ZBTZBHZBIZBSBSEzcawBSEzyzuawac`.

After that I just reversed the encryption process in the python script.

```python
import string
# ⠱⠁ ⠹⠣ ⠱⠹ ⠱⠁ ⠹⠣ ⠹⠳ ⠱⠁ ⠹⠣ ⠹⠪ ⠱⠁ ⠹⠣ ⠱⠩ ⠹⠣ ⠱⠩ ⠹⠱ ⠻⠁ ⠫⠩ ⠫⠡ ⠻⠻ ⠹⠣ ⠱⠩ ⠹⠱ ⠻⠁ ⠻⠪ ⠻⠁ ⠻⠱ ⠫⠡ ⠻⠻ ⠫⠡ ⠫⠩
# https://www.dcode.fr/gs8-braille-code
# s = "5a42545a42485a42495a42534253457a6361774253457a797a7561776163"
# print(bytes.fromhex(s).decode())
# ZBTZBHZBIZBSBSEzcawBSEzyzuawac

upperFlag = string.ascii_uppercase[:26]  # all
lowerFlag = string.ascii_lowercase[:26]  # all
MIN_LETTER = ord("a")
MIN_CAPLETTER = ord("A")


def unpuzzle(puzzeled):
    to_unp = ""
    i = 0
    while i < len(puzzeled):
        if puzzeled[i].isupper():
            if puzzeled[i]+puzzeled[i+1]+puzzeled[i+2] == "CTF":
                to_unp += "_"
            else:
                binary = "{0:05b}".format(upperFlag.index(puzzeled[i]))+"{0:05b}".format(
                    upperFlag.index(puzzeled[i+1]))+"{0:005b}".format(upperFlag.index(puzzeled[i+2]))
                to_unp += chr(int(binary, 2))
            i += 3
            # print(puzzeled[i-3:i])
        elif puzzeled[i].islower():
            binary = "{0:01x}".format(lowerFlag.index(
                puzzeled[i])) + "{0:01x}".format(lowerFlag.index(puzzeled[i+1]))
            to_unp += chr(int(binary, 16))
            i += 2
            print(puzzeled[i-2:i])
    return to_unp


def mix(oneLetter, num):
    if (oneLetter.isupper()):
        word = ord(oneLetter)-MIN_CAPLETTER
        shift = ord(num)-MIN_CAPLETTER
        return upperFlag[(word - shift) % len(upperFlag)]
    if (oneLetter.islower()):
        word = ord(oneLetter)-MIN_LETTER
        shift = ord(num)-MIN_LETTER
        return lowerFlag[(word - shift) % len(upperFlag)]


enc = "ZBTZBHZBIZBSBSEzcawBSEzyzuawac"
for key in lowerFlag:
    flag = ""
    print("Key: ", key)
    for count, c in enumerate(enc):
        flag += mix(c, key)
    print(flag)
    print("FLAG: ", unpuzzle(flag))
```

Running the script, the only human readable result is `Key:  t` and `FLAG: THIS_is_easy`. Just make sure to wrap it in the flag format.

## Flag

`TUCTF{THIS_is_easy}`
