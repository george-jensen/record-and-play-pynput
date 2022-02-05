![Header](READMEHeader.png "Header")

This allows you to record keyboard and mouse input, and play it back (with looping) using pynput. It allows for automation of any repetitive computer tasks.

<h1>Installation</h1>

- Clone or download this repository
- Navigate to the repository in cmd or terminal
- Run pip install -r requirements.txt

<h1>Usage</h1>

- Simply run the 'record.py' file with Python3 using an input argument -> "name_of_recording" and a second optional argument 'record-all' (for more information on 'record-all' read the notes below). All keyboard and mouse activity after this command will be recorded.
- To end the recording click the escape key (to end the Keyboard thread), and hold down the right click on the mouse for more than 2 seconds (without moving the mouse) - then release (to end the Mouse thread).
- To play back the recording, run the 'play.py' file with Python3 using two input arguments -> 'name_of_recording' 'number_of_repeats'.

If you want to kill the play-back early, you can trigger a KeyboardInterrupt by clicking into the terminal window and pressing 'ctrl c' - although you'll have to do this while the automation is running.

<h2>Notes</h2>

The 'record-all' parameter means all mouse movement will be recorded, as well as clicks and keyboard. If your recording is very lenghty (i.e. 30+ minutes with a lot of mouse movement) then your data file will be several megabytes, if you'd rather it not be this large then I'd advise not including this optional parameter and the program will only record the mouse movement for dragging (clicks and their location will still be recorded, as well as all keyboard input and scrolling).

Scrolling functionality is supported, however it is not completely precise, due to the carry through nature of scrolling on many applications. So it is recommended to drag scrollbars when available. If you find you need to scroll to the top or bottom of pages then try and over-compensate when recording before continuing.

<h2>Compatablitity</h2>

This is both Windows and Mac compatible - I haven't been able to find a Mac compatible tool that does a similar job and that is one of the reasons for this repository's creation.

<h2>Authors</h2>
George Jensen

<h2>Support!</h2>
If you found this tool useful please give this repo a star!

Please also feel free to create an issue to give feedback on any bugs, or ask for improvements! I'm always keen to keep things up to date and useful so any and all feedback is welcome!
