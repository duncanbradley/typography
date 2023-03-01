# Climate Crisis Variable Font Animation

Variable font animation of historical data and predictions for Arctic Sea Ice Extent (1979-2050):


<img src="https://github.com/duncanbradley/typography/blob/main/ice.gif" alt="Animated gif, with the words Artic Sea Ice and a year, starting at 1979 and increasing by 1 until 2050. The typeface starts with a very heavy weight but the thickness of the characters shrinks over time. By 2050, the text has the fragile appearance of thawing ice." width="500" />

Step By Step:
1. [Install Climate Crisis Font](https://kampanjat.hs.fi/climatefont/index.html)
2. [Install Coldtype Python library](https://coldtype.goodhertz.com/install.html) (contains video tutorial)
3. Navigate to appropriate directory and then`source venv/bin/activate` (“the magical incantation” for xxx)
4. `coldtype climate-crisis` to launch to viewer
5. Press spacebar to play and pause
6. `coldtype —render climate-crisis` to render each frame in new folder
7. Navigate into new folder and `convert -loop 4 *.png ice.gif` to create .gif
