bk
---

An utility that lets you change desktop background for GNU/Linux and Windows.

### Features

- Support for multi monitor environments
- Straightforward CLI parameters
- Fitting wallpaper to desktop (`--fit`)
- Covering whole desktop (`--cover`)
- Scaling the image by percentage (`--scale 0.5 0.5` to scale to 50% of
  original size)
- Cropping the image by percentage (`--crop 0.2 0.2 0.8 0.8` to crop 20% from
  each side)
- Preserving virtual border (`--gap 10 20 30 40` to take pixels from each side
  in clockwise manner)
- Setting solid backgrounds (`--background orange`)
- Borders (`--border-color black --border-size 2`)
- Downloading images from the Internet

### Example

    bk set 2 minako.png \
        --background lemonchiffon \
        --border-size 2 --border-color maroon \
        --translate 1 0 \
        --gap 100 100 100 100

Will set `minako.png` on second monitor without doing scaling of any sort,
moving it to upper right corner but maintaining 100 pixels gap from each side,
adding 2px dark red border and using light yellow color as background color.
Result:

![result](https://cloud.githubusercontent.com/assets/1045476/8054172/c4ffe1a0-0e96-11e5-8e3b-3f97df75f84e.jpg)

### Requirements

- Python 3
- PIL (`pip install pillow`)

Specific to GNU/Linux:

- X11 + Xinerama
- feh (`pacman -S feh`, `apt-get install feh`)

Specific to MS Windows:

- Cygwin (will probably support native Python as well at some point)
- Powershell

### Limitations

- Windows users need Cygwin
- Can't set one wallpaper across multiple monitors
- Can't set wallpaper image from clipboard
