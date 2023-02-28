# Climate Crisis Variable Font Animation

Variable font animation of historical data and predictions for Arctic Sea Ice Extent (1979-2050):

[gif]

Step By Step:
1. Install Climate Crisis Font (link)
2. Install Coldtype (link) Python library - see tutorial (link)
3. Navigate to appropriate directory and then`source venv/bin/activate` (“the magical incantation” for xxx)
4. `coldtype climate-crisis` to launch to viewer
5. Press spacebar to play and pause
6. `coldtype —render climate-crisis` to render each frame in new folder
7. Navigate into new folder and `convert -loop 4 *.png ice.gif` to create .gif
