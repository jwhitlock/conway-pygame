# Conway's Game of Life

This is
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life),
written in PyGame.

It was developed on:

* [pygame](https://github.com/pygame/pygame) 2.0.0.dev6. 1.9.6 (stable) gave a blank grey screen.
* SDL 2.0.10, installed with Homebrew
* macOS 10.14.6 (Mojave)
* Python 3.7.6

# Install

* Install SDL 2 with [Homebrew](https://docs.brew.sh/Installation):
    ```
    brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf
    ```
* Install ``pyenv`` and Python 3.7.6:
    ```
    brew install pyenv
    pyenv install 3.7.6
    pyenv shell 3.7.6
    ```
* Create a ``virtualenv``:
    ```
    virtualenv .venv
    source .venv/bin/activate
    ```
* Install ``pygame``:
    ```
    pip install -r requirements.txt
    ```
* Run it!
    ```
    ./conway.py
    ```

## Commands

* **Mouse click** - Recreate random grid
* **Any key** - Quit




