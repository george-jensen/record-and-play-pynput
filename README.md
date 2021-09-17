# record-and-play-pynput
This allows you to record keyboard and mouse input, and play it back (with looping) using pynput. It allows for automation of any repetitive computer tasks.

<h1>Usage</h1>

- Clone the repository
- Simply run the 'record.py' file with Python3 using one input argument -> "name_of_recording". Whatever you do thereafter will be recorded.
- To end the recording click the escape key (to end the Keyboard thread), and use the scroll on the mouse (to end the Mouse thread).
- To play back the recording, run the 'play.py' file with Python3 using two input arguments -> "name_of_recording" 'number_of_repeats'.

If you want to kill the play-back early, you can trigger a KeyboardInterrupt by clicking into the terminal window and pressing 'ctrl c' - although you'll have to do this while the automation is running.

<h2>Notes</h2>

- The data file takes in mouse movements every 50th of a second when holding down the left click on the mouse (dragging). If you aren't dragging a lot then you can run a relatively lengthy automation without creating a huge data file, however, if you're dragging a lot, keep the recording relatively short, as the data file will quickly fill up with mouse-movement JSON data.

*Scrolling is not supported, as it is used to halt the Mouse listener. This may be adjusted later to support scrolling.

<h2>Compatablitity</h2>

This is Mac compatiable – as I haven't been able to find others out there that are.
