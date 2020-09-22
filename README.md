# Welcome! #

## The Problem ##

Imagine a world where Rectangle Editing Software is a thing. Those type of programs
are specialized CAD software to create and manage drawings of rectangles, where users
can carefully design their rectangular layouts and save them as project files. There are
two main market leaders on this highly competitive segment: Quadium and RectStar.

Those two programs, although very similar in function, produce two completely different files
when saving a rectangle project. You are hired as a programmer for a company that converts
between those two CAD programs, and sells that as a service to the customers that want to 
 migrate their projects into another editor.
 
In order to do that conversion between formats, the company must first produce an independent
representation of the data from both formats, that can be later converted to either one.

Rectangle projects usually have a background color, and several rectangles positioned on top
of it, with varying rotations.

An example of the internal representation and the two other files can be found on the
`example_files` folder. Those three files all represent the **same** project.

## Your Task ##

You are asked to develop a tool utility to decode rectangle projects from those two CAD 
formats into the internal representation.

Your program will be run via the `app.py` script, where a file saved either on RectStar or Quadium
will be provided via command-line arguments, and the tool will convert it into the internal
representation and output it to stdout (print).

Mind you that you should not change the command-line interface of the application, as it is
expected to be used like that by other parts of the solution (and you will fail all the 
automated tests).

## About the internal file

The internal file, produced after converting either one of the other two CAD formats, consist of a 
JSON with the following schema:

| name                  | type               | description                                                                             |
|-----------------------|--------------------|-----------------------------------------------------------------------------------------|
| bg                    | string             | The background color of the design                                                      |
| rectangles            | List[Rectangle]    | A list of rectangle objects                                                             |
| rectangles[].point    | List[float, float] | The x,y position of the rectangle on the canvas,considering the lower-left corner of it.|
| rectangles[].width    | float              | The width of the rectangle                                                              |
| rectangles[].rotation | float              | Rotation, in degrees, of the rectangle. The pivot point is the same, lower-left corner. |
| rectangles[].color    | string             | The color of the rectangle                                                              | 

The canvas has its origin on the lower-left corner, as do the rectangles themselves.

## About the Quadium file

The Quadium file is somewhat documented by the manufacturer, and we know that rectangles
are described with their center-point plus width and height. This means that the coordinates would
change, and some transformations would have to be done when converting it into our internal format, 
specially with regards to rotations.

Also, Quadium has the concept of Squares, which our internal format generalizes into normal rectangles.

## About the RectStar file

Nothing is known about RectStar files. Luckily, we were able to get the same project saved on
RectStar, Quadium and our internal file format, so you can derive conclusions from comparing them.
Those files are on the `example_files` folder.

## How to test ##

Just feed the cad file into `app.py` (like below), and check if the output of both files match the
internal representation:

```shell script
python app.py --type=rect_star example_files/sample.rstar
python app.py --type=quadium example_files/sample.quadium
```

## How to install and run ##

Just install the dependencies are on `requirements.txt`, and run the main file (app.py).