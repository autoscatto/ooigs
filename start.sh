#!//bin/bash
mkdir -p tmp
rm -rf tmp/*
mkdir -p pdf
rm -rf pdf/*
python qr.py
montage tmp/*.png  -tile 1x3  -geometry 497x584+0+0  miff:- |montage - -geometry +0+0 -tile 2x1 miff:- |convert - -resize 1240x1753 -extent 1240x1753 -gravity center -units PixelsPerInch -density 150x150 pdf/Gif.pdf

