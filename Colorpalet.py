darkGrey = '#%02x%02x%02x' % (184, 184, 184)
darkPurple = '#%02x%02x%02x' % (102, 51, 153)
white = '#%02x%02x%02x' % (255, 255, 255)

limeGreen = '#%02x%02x%02x' % (128, 201, 4)
darkGreen = '#%02x%02x%02x' % (102, 161, 3)

darkRed = '#%02x%02x%02x' % (204, 0, 0)
lightRed = '#%02x%02x%02x' % (255, 0, 0)

lightBlue = '#%02x%02x%02x' % (66, 158, 189)
darkBlue = '#%02x%02x%02x' % (8, 54, 193)

darkBgColor = '#%02x%02x%02x' % (54, 54, 54)
lightBgColor = '#%02x%02x%02x' % (220, 220, 220)

windowBgDark = '#%02x%02x%02x' % (24, 24, 24)
windowBgLight = '#%02x%02x%02x' % (240, 240, 240)

mainBgColor = lightBgColor
windowBgColor = windowBgLight

buttonColor = lightBlue
buttonText = white


def setDarkMode():
    global mainBgColor
    mainBgColor = darkBgColor
    global windowBgColor
    windowBgColor = windowBgDark
    global buttonColor
    buttonColor = darkPurple


def setLightMode():
    global mainBgColor
    mainBgColor = lightBgColor
    global windowBgColor
    windowBgColor = windowBgLight
    global buttonColor
    buttonColor = lightBlue
