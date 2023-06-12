# Secret Kitten

## Challenge

We get a photo of a kitten and a hint that the flag is hidden in the image.

## Solution

Standard stego challenge. I run `binwalk` on the image and find a 7zip file hidden in the image. Running `binwalk -e` extracts the file. Inside the extracted folder we have the flag file.

### Flag

`TUCTF{PLZ_P37_7H3_K1773H_45729}`
