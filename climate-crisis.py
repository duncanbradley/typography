from coldtype import *
from coldtype.fx.skia import phototype, spackle, luma, fill, precompose
from coldtype.fx.motion import filmjitter
from coldtype.warping import warp

fnt = Font.Cacheable("ClimateCrisis-Variable.ttf")
poppins = Font.Cacheable("Poppins-Medium.ttf")

@animation(timeline=215, composites=1, bg =0.1, render_bg=1)

def thumbnail(f):
    r = f.a.r
    yr = round(f.i/3) + 1979

    border = P().rect(r.inset(60)
        .subtract(80, "N")
        .subtract(80, "S")
        ).fssw(-1, 0.9, 3)
        
    caption = (StSt("Animation by @duncanbradley_\nClimate Crisis Font by Eino Korkala and Daniel Coull", poppins, 15,
    leading = 60)).f(0.9).track(-50, v=1).xalign(r.inset(60), "E")

    ASI = (StSt("Arctic\nSea Ice",
            fnt, 150, wght=1, slnt=1, leading=-200,
            year = f.e("qeio", 0.5))
            .f(1)
            .align(r)
            .reversePens()
            .distribute(v=1)
            .track(-125, v=1)
            .xalign(r.inset(140+(f.i/8)), "W")
            )

    ASIT = (StSt("Arctic\nSea Ice",
            fnt, 150, wght=1, slnt=1, leading=40,
            year = 0)
            .f(0.15)
            .align(r)
            )

    YEAR = (StSt(str(round(f.e("qeio", 0.5)*71+1979)), fnt, 200,
            tu=-10, r=1, ro=1, wdth=0.65,
            year = f.e("linear", 0.5))
            .align(r)
            .f(1))

    return (PS([
        ASIT,
        YEAR,
        ])
        .reversePens()
        .distribute(v=1)
        .track(-150, v=1)
        .align(r)
        .xalign(r.inset(140), "W")
        .append(ASI)
        .insert(1, border)
        .insert(1, caption))

release = thumbnail.export("gif")
# press r in viewer to render all images to in folder
# then in thumbnail folder in terminal run following code: convert -loop 4 *.png screens.gif
# requires ImageMagick 
