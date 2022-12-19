import PySimpleGUI as sg
import os

def init(id):
    fileName = "stormworks64.exe"
    makeBakup = False
    patches = [
        [
            b"\x00Stormworksk\x00",
            b"\x00Stormworks\x00",
        ],
        [
            b"\x00Report Bug / Request Featurek\x00",
            b"\x00Report Bug / Request Feature\x00",
        ],
        [
            b"\x00Join us on Discordk\x00",
            b"\x00Join us on Discord\x00",
        ],
        [
            b"\x00Steam Workshopk\x00",
            b"\x00Steam Workshop\x00",
        ],
        [
            b"\x00Video Tutorialsk\x00",
            b"\x00Video Tutorials\x00",
        ],
        [
            b"\x2069Bit\x00",
            b"\x2064Bit\x00",
        ],
        [
            b"\x00v1.6.9\x00",
            b"\x00v1.6.9\x00",
        ],
        [
            b"\x00Tile Editor\x00",
            b"\x00Tile Editor\x00",
        ],
        [
            b"\x00Component Editor\x00",
            b"\x00Component Editor\x00",
        ],
        [
            (76561197976988654).to_bytes(8, byteorder = "little"),
            (int(id)).to_bytes(8, byteorder = "little"),
        ],
    ]

    print(patches)

    with open(fileName,"rb") as file:
        content = file.read()
    newContent = bytearray(content)
    for patch in patches:
        old = patch[0]
        oldLen = len(old)
        new = patch[1]
        newLen = len(new)
        if newLen > oldLen:
            try:
                print(f"Error {new.decode('utf-8')} is bigger than {old.decode('utf-8')}")
            except:
                print(f"Error {new} is bigger than {old}")
        offset = content.find(old)
        if offset != -1:

            for i in range(0, newLen):
                newContent[i + offset] = new[i]

            for i in range(offset + newLen, offset + oldLen):
                newContent[i] = b"\x00"[0]
        else:
            try:
                print(f"Error Could not find {old.decode('utf-8')}")
            except:
                print(f"Error Could not find {old}")
            continue

    if makeBakup:
        bakcount = 0
        for file in os.listdir():
            if ".bak" in file:
                bakcount += 1
        with open(fileName + ".bak" + str(bakcount),"wb") as file:
            file.write(content)

    with open(fileName,"wb") as file:
        file.write(newContent)

    print("Finished")

def main():
    layout = [  [sg.Button('Exit')],[sg.Button('Eject')],[sg.Text('SteamID')],[sg.InputText(key='-CDINPUT-')              ]] 
    window = sg.Window('Dev_mode by Titan and Dr42', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        id = values['-CDINPUT-']
        if event == sg.WIN_CLOSED or event == 'Eject':
            init(id)
main()