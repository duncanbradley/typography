# Climate Crisis Variable Font Animation

Variable font animation of historical data and predictions for Arctic Sea Ice Extent (1979-2050):

[gif]

Step By Step:
1. [Install Climate Crisis Font](https://kampanjat.hs.fi/climatefont/index.html)
2. [Install Coldtype Python library](https://coldtype.goodhertz.com/install.html) (contains video tutorial)
3. Navigate to appropriate directory and then`source venv/bin/activate` (“the magical incantation” for xxx)
4. `coldtype climate-crisis` to launch to viewer
5. Press spacebar to play and pause
6. `coldtype —render climate-crisis` to render each frame in new folder
7. Navigate into new folder and `convert -loop 4 *.png ice.gif` to create .gif
