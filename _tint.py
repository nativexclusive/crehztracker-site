"""Re-skin the App Store screenshots into the app's palettes, the way the app
does it (palShiftWith): low-chroma pixels take the palette's neutral hue, the
warm accent family (copper, amber) takes the accent hue, greens/reds/blues are
left alone. Hues here are HSL approximations of the OKLCH table."""
import sys, os
from PIL import Image, ImageChops
SRC="build/appstore-6.9-b182"; OUT="site/img"
PAL={ # key: (neutral hue°, neutral chroma x, accent hue°, accent chroma x)
 'periwinkle':(237,1.5,243,1.2),'lagoon':(183,1.5,187,.85),'blush':(350,1.6,318,1.0),
 'violet':(285,1.1,285,1.15),'arctic':(205,.6,198,.77),'sand':(42,1,28,1)}
JOBS={'periwinkle':['01-overview','02-expenses','03-income','05-home-office','06-1099-recipients','07-reporting-analytics'],
      'lagoon':['01-overview','02-expenses','03-income','06-1099-recipients','07-reporting-analytics'],'blush':['01-overview'],'violet':['01-overview','02-expenses','03-income'],'arctic':['01-overview','02-expenses','03-income','04-mileage']}
# 01-03 are device captures (9:02, no island); 04-07 carry the 9:41 bar with the island.
# Every screen gets 04's top strip so the phones match.
STRIP=Image.open(f"{SRC}/04-mileage.png").convert('RGB').crop((0,0,1320,175))
def h8(deg): return int(round(deg/360*255))%256
def tint(im,nH,nC,aH,aC):
    hsv=im.convert('HSV'); H,S,V=hsv.split()
    neutral=S.point(lambda v:255 if v<64 else 0)                    # S < .25
    warmhue=H.point(lambda v:255 if h8(8)<=v<=h8(62) else 0)         # 8°..62°
    warm=ImageChops.multiply(warmhue, S.point(lambda v:255 if v>=64 else 0))
    H2=Image.composite(Image.new('L',H.size,h8(nH)),H,neutral)
    H2=Image.composite(Image.new('L',H.size,h8(aH)),H2,warm)
    S2=Image.composite(S.point(lambda v:min(255,int(v*nC))),S,neutral)
    S2=Image.composite(S.point(lambda v:min(255,int(v*aC))),S2,warm)
    return Image.merge('HSV',(H2,S2,V)).convert('RGB')
for pal,names in JOBS.items():
    os.makedirs(f"{OUT}/{pal}",exist_ok=True)
    for n in names:
        im=Image.open(f"{SRC}/{n}.png").convert('RGB')
        im.paste(STRIP,(0,0))                      # one status bar (9:41 + island) on every screen
        im.thumbnail((660,10000),Image.LANCZOS)
        tint(im,*PAL[pal]).save(f"{OUT}/{pal}/{n}.jpg",quality=82,optimize=True)
        print(pal,n)
