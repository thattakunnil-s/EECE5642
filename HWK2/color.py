from PIL import Image

def scaleRGB(r, g, b):
    r_norm = r / 255
    g_norm = g / 255
    b_norm = b / 255

    return round(r_norm, 3), round(g_norm, 3), round(b_norm, 3)


def cmyk(r_norm, g_norm, b_norm):
    c = 1 - r_norm
    m = 1 - b_norm
    y = 1 - g_norm
    k = min(c, m, y)

    if(k == 1):
        c, m, y, k = 0
    else:
        c = (c - k)/(1 - k)
        m = (m - k)/(1 - k)
        y = (y - k)/(1 - k)

    return round(c*100), round(m*100), round(y*100), round(k*100)


def XYZ(r_norm, g_norm, b_norm):
    v = [r_norm, g_norm, b_norm]

    for i in range(len(v)):
        if( v[i] > 0.04045):
             v[i] = ((v[i] + 0.055) / 1.055) ** 2.4
        else:
             v[i] = v[i] / 12.92

    var_R = v[0] * 100
    var_G = v[1] * 100
    var_B = v[2] * 100

    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

    return round(X,3), round(Y,3), round(Z,3)


def xyY(X, Y, Z):
    Y = Y
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)

    return round(x,3), round(y,3), round(Y,3)


def hsv(var_R, var_G, var_B):
    var_Min = min(var_R, var_G, var_B) # Min.value of RGB
    var_Max = max(var_R, var_G, var_B) # Max.value of RGB
    del_Max = var_Max - var_Min # Delta RGB value

    V = var_Max

    if(del_Max == 0):   # This is a gray, no chroma
        H, S = 0, 0
    else:             # Chromatic data
        S = del_Max / var_Max
        del_R = (((var_Max - var_R) / 6) + (del_Max / 2)) / del_Max
        del_G = (((var_Max - var_G) / 6) + (del_Max / 2)) / del_Max
        del_B = (((var_Max - var_B) / 6) + (del_Max / 2)) / del_Max

        if(var_R == var_Max):
            H = del_B - del_G
        elif(var_G == var_Max):
            H = (1 / 3) + del_R - del_B
        elif(var_B == var_Max):
            H = (2 / 3) + del_G - del_R

        if(H < 0):
            H += 1
        if(H > 1):
            H -= 1

    return round(H,3), round(S,3), round(V,3)


def hsl(var_R, var_G, var_B):
    var_Min = min(var_R, var_G, var_B) # Min.value of RGB
    var_Max = max(var_R, var_G, var_B) # Max.value of RGB
    del_Max = var_Max - var_Min # Delta RGB value

    L = (var_Max + var_Min) / 2

    if(del_Max == 0):   # This is a gray, no chroma
        H, S = 0, 0
    else:             # Chromatic data
        if(L < 0.5):
            S = del_Max / ( var_Max + var_Min )
        else:
            S = del_Max / ( 2 - var_Max - var_Min )

        del_R = (((var_Max - var_R) / 6) + (del_Max / 2)) / del_Max
        del_G = (((var_Max - var_G) / 6) + (del_Max / 2)) / del_Max
        del_B = (((var_Max - var_B) / 6) + (del_Max / 2)) / del_Max

        if(var_R == var_Max):
            H = del_B - del_G
        elif(var_G == var_Max):
            H = (1 / 3) + del_R - del_B
        elif(var_B == var_Max):
            H = (2 / 3) + del_G - del_R

        if(H < 0):
            H += 1
        if(H > 1):
            H -= 1

    return round(H, 3), round(S, 3), round(L, 3)


def createImage(r, g, b):
    rgb = (r, g, b)
    size = (300, 150)
    image = Image.new("RGB", size, rgb)
    return image

r, g, b = 137, 56, 146
print(f"RGB colors : ({r},{g},{b})")
r_norm, g_norm, b_norm = scaleRGB(r, g, b)
print(f"RGB scaled to [0,1] : ({r_norm},{g_norm},{b_norm})")
c, m, y, k = cmyk(r_norm, g_norm, b_norm)
print(f"CMYK : ({c},{m},{y},{k})")
X, Y, Z = XYZ(r_norm, g_norm, b_norm)
print(f"CIE XYZ : ({X},{Y},{Z})")
x, y, Y = xyY(X, Y, Z)
print(f"CIE xyY : ({x},{y},{Y})")
H, S, V = hsv(r_norm, g_norm, b_norm)
print(f"HSV : ({H},{S},{V})")
H, S, L = hsl(r_norm, g_norm, b_norm)
print(f"HSL : ({H},{S},{L})")
colorImage = createImage(r, g, b)
colorImage.show()
colorImage.save("DV_steffi_color.png")
