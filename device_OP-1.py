# name=Teenage Engineering OP-1
# url=https://github.com/ryrun/FL-OP1-controller-script

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
            # 39 = play button
            if event.data1 == 39:
                transport.start()
                event.handled = True
            # 40 = stop button
            elif event.data1 == 40:
                transport.stop()
                event.handled = True
            # 38 = record button
            elif event.data1 == 38:
                transport.record()
                event.handled = True
            # 6 = metronome button
            elif event.data1 == 6:
                transport.globalTransport(midi.FPT_Metronome, 1, event.pmeFlags)
                event.handled = True
            # 10 = mixer button = show fl mixer
            elif event.data1 == 10:
                transport.globalTransport(midi.FPT_F9, 1, event.pmeFlags)
                event.handled = True
            # 9 = tape button = show fl playlist
            elif event.data1 == 9:
                transport.globalTransport(midi.FPT_F5, 1, event.pmeFlags)
                event.handled = True
            # 8 = drum button = show fl channel rack
            elif event.data1 == 8:
                transport.globalTransport(midi.FPT_F6, 1, event.pmeFlags)
                event.handled = True