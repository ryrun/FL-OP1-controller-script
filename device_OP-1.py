# name=Teenage Engineering OP-1
# url=

import fl
import patterns
import mixer
import device
import transport
import arrangement
import general
import launchMapPages
import playlist
import midi
import utils


def OnMidiMsg(event):
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data2 > 0:
            if event.data1 == 39:
                transport.start()
                event.handled = True
            elif event.data1 == 40:
                transport.stop()
                event.handled = True
            elif event.data1 == 38:
                transport.record()
                event.handled = True
            elif event.data1 == 6:
                transport.globalTransport(midi.FPT_Metronome, 1, event.pmeFlags)
                event.handled = True
