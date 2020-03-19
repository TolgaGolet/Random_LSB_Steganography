import binascii, cv2, random

def convertStringToBinary(string):
    return bin(int.from_bytes(string.encode(), 'big'))

def convertBinaryToString(binary):
    n = int(binary, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

imageName = 'hidden.bmp'

originalImage = cv2.imread(imageName)
image = cv2.imread(imageName)
height, width = image.shape[:2]

bitsMessageSize = int(input('Enter the hidden message size in bits: '))

key = -1
passed = False
while key <= 0 or key >999:
    if passed == True:
        print('Invalid key. It should be an integer and maximum 3 digits long')
    key = int(input('\nEnter the encryption key: '))
    passed = True

random.seed(key) #The same random numbers every time
#Unique numbers
randomLocations = random.sample(range(height * width), k = int(bitsMessageSize / 3) + 1)
#print("lenrandomLocations:", len(randomLocations))

#Pixel locations of random locations
pixelLocations = []

for randomLocation in randomLocations:
    pixelLocations.append(int(randomLocation / height) % height) #i
    pixelLocations.append(randomLocation % width) #j
#print("lenpixelLocations:", len(pixelLocations))

index = 0  #Loop index
messageIndex = 2
binaryMessage = '0b'
readBits = 0
percentPart = 100 / bitsMessageSize
percentage = 0
print(str(int(percentage))+"% complete", end="\r")

for w in range(0, len(pixelLocations), 2):
    if w <= len(pixelLocations)-2:
        i = pixelLocations[w]
        j = pixelLocations[w + 1]
        if index >= bitsMessageSize:
            #print('İkinci ife girdi')
            break
        pixelValues = image[i,j]
        #print(pixelValues, 'h:', i, 'w:', j)
        #BGR
        for l in range(3):
            if (messageIndex - 2) >= bitsMessageSize:
                #print('Üçüncü ife girdi')
                break
            elif l == 0:
                print(str(int(percentage))+"% complete", end="\r")
                binaryMessage += bin(image[i, j][0])[-1]
                readBits += 1
                percentage += percentPart
            elif l == 1:
                print(str(int(percentage))+"% complete", end="\r")
                binaryMessage += bin(image[i, j][1])[-1]
                readBits += 1
                percentage += percentPart
            elif l == 2:
                print(str(int(percentage))+"% complete", end="\r")
                binaryMessage += bin(image[i, j][2])[-1]
                readBits += 1
                percentage += percentPart
            messageIndex += 1
    else:
        #print('ilk ife giremedi')

        index += 1

print("100% complete")
print("readBits:", readBits)
print("lenbinarymessage:", len(binaryMessage[2::]))
print('Binary message:', binaryMessage[2::])
print('Hidden data:', convertBinaryToString(binaryMessage[2::]))
