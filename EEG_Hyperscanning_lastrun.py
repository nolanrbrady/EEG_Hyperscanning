#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Tue Jun 28 18:58:54 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'EEG_Hyperscanning'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nolanbrady/Desktop/LabResearch/EEG_Protocols/EEG_Hyperscanning/EEG_Hyperscanning_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "load_triggers"
load_triggersClock = core.Clock()
from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name="Trigger", type="Markers", channel_count=1, channel_format='int32', source_id="Aurora")
outlet = StreamOutlet(info)

# Initialize components for Routine "trial"
trialClock = core.Clock()
intro = visual.TextStim(win=win, name='intro',
    text='Welcome to the EEG Hyperscanning task\n\nThe first block will be simple hand motions such as open and closed fists and hand rotation.\n\nThe second block will include more complicated hand motions such as different numbers of fingers displayed on the hand.\n\nEach different task will include a rest block in between where you will simply look at the center of the screen idely.\n\nPress Spacebar to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next = keyboard.Keyboard()

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please relax and look at the center of the screen for 15 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('baseline.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "simple_nonsync"
simple_nonsyncClock = core.Clock()
start_sound = sound.Sound('simple_nonsync.wav', secs=-1, stereo=True, hamming=True,
    name='start_sound')
start_sound.setVolume(1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please do non-synchronized simple movements for 90 seconds. Please listen for the tone to start.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "simple_timing"
simple_timingClock = core.Clock()
sound_8 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
sound_9 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
sound_10 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_10')
sound_10.setVolume(1.0)
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)
sound_14 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_14')
sound_14.setVolume(1.0)
sound_15 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_15')
sound_15.setVolume(1.0)
sound_16 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_16')
sound_16.setVolume(1.0)
sound_17 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_17')
sound_17.setVolume(1.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Please alternate hand signal after each beep.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please relax and look at the center of the screen for 15 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('baseline.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "complex_nonsync"
complex_nonsyncClock = core.Clock()
start_sound_2 = sound.Sound('complex_nonsync.wav', secs=-1, stereo=True, hamming=True,
    name='start_sound_2')
start_sound_2.setVolume(1.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='Please do non-synchronized complex hand motions for 90 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "complex_timing"
complex_timingClock = core.Clock()
sound_7 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
sound_18 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_18')
sound_18.setVolume(1.0)
sound_19 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_19')
sound_19.setVolume(1.0)
sound_20 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_20')
sound_20.setVolume(1.0)
sound_21 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_21')
sound_21.setVolume(1.0)
sound_22 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_22')
sound_22.setVolume(1.0)
sound_23 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_23')
sound_23.setVolume(1.0)
sound_24 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_24')
sound_24.setVolume(1.0)
sound_26 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_26')
sound_26.setVolume(1.0)
sound_25 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_25')
sound_25.setVolume(1.0)
sound_27 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_27')
sound_27.setVolume(1.0)
sound_31 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_31')
sound_31.setVolume(1.0)
sound_32 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_32')
sound_32.setVolume(1.0)
sound_30 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_30')
sound_30.setVolume(1.0)
sound_35 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_35')
sound_35.setVolume(1.0)
sound_34 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_34')
sound_34.setVolume(1.0)
sound_33 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_33')
sound_33.setVolume(1.0)
sound_29 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_29')
sound_29.setVolume(1.0)
sound_28 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_28')
sound_28.setVolume(1.0)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Please alternate hand position after every beep.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please relax and look at the center of the screen for 15 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('baseline.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "sync_complex_A"
sync_complex_AClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Participant A, please do complex hand motions for 90 seconds. Participant B, please imitate.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_3 = sound.Sound('sync_complex_A.wav', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)

# Initialize components for Routine "complex_timing"
complex_timingClock = core.Clock()
sound_7 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
sound_18 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_18')
sound_18.setVolume(1.0)
sound_19 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_19')
sound_19.setVolume(1.0)
sound_20 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_20')
sound_20.setVolume(1.0)
sound_21 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_21')
sound_21.setVolume(1.0)
sound_22 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_22')
sound_22.setVolume(1.0)
sound_23 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_23')
sound_23.setVolume(1.0)
sound_24 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_24')
sound_24.setVolume(1.0)
sound_26 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_26')
sound_26.setVolume(1.0)
sound_25 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_25')
sound_25.setVolume(1.0)
sound_27 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_27')
sound_27.setVolume(1.0)
sound_31 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_31')
sound_31.setVolume(1.0)
sound_32 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_32')
sound_32.setVolume(1.0)
sound_30 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_30')
sound_30.setVolume(1.0)
sound_35 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_35')
sound_35.setVolume(1.0)
sound_34 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_34')
sound_34.setVolume(1.0)
sound_33 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_33')
sound_33.setVolume(1.0)
sound_29 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_29')
sound_29.setVolume(1.0)
sound_28 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_28')
sound_28.setVolume(1.0)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Please alternate hand position after every beep.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please relax and look at the center of the screen for 15 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('baseline.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "sync_complex_b"
sync_complex_bClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Participant B, please do complex hand motions for 90 seconds. Participant A, please imitate.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_4 = sound.Sound('sync_complex_B.wav', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)

# Initialize components for Routine "complex_timing"
complex_timingClock = core.Clock()
sound_7 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
sound_18 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_18')
sound_18.setVolume(1.0)
sound_19 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_19')
sound_19.setVolume(1.0)
sound_20 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_20')
sound_20.setVolume(1.0)
sound_21 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_21')
sound_21.setVolume(1.0)
sound_22 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_22')
sound_22.setVolume(1.0)
sound_23 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_23')
sound_23.setVolume(1.0)
sound_24 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_24')
sound_24.setVolume(1.0)
sound_26 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_26')
sound_26.setVolume(1.0)
sound_25 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_25')
sound_25.setVolume(1.0)
sound_27 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_27')
sound_27.setVolume(1.0)
sound_31 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_31')
sound_31.setVolume(1.0)
sound_32 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_32')
sound_32.setVolume(1.0)
sound_30 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_30')
sound_30.setVolume(1.0)
sound_35 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_35')
sound_35.setVolume(1.0)
sound_34 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_34')
sound_34.setVolume(1.0)
sound_33 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_33')
sound_33.setVolume(1.0)
sound_29 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_29')
sound_29.setVolume(1.0)
sound_28 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_28')
sound_28.setVolume(1.0)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Please alternate hand position after every beep.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please relax and look at the center of the screen for 15 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('baseline.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "sync_simple_A"
sync_simple_AClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Participant A, please do simple hand motions for 90 seconds. Participant B, please imitate.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_5 = sound.Sound('sync_simple_A.wav', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)

# Initialize components for Routine "simple_timing"
simple_timingClock = core.Clock()
sound_8 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
sound_9 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
sound_10 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_10')
sound_10.setVolume(1.0)
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)
sound_14 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_14')
sound_14.setVolume(1.0)
sound_15 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_15')
sound_15.setVolume(1.0)
sound_16 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_16')
sound_16.setVolume(1.0)
sound_17 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_17')
sound_17.setVolume(1.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Please alternate hand signal after each beep.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please relax and look at the center of the screen for 15 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('baseline.wav', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "sync_simple_b"
sync_simple_bClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Participant B, please do simple hand motions for 90 seconds. Participant A, please imitate.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_6 = sound.Sound('sync_simple_B.wav', secs=-1, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)

# Initialize components for Routine "simple_timing"
simple_timingClock = core.Clock()
sound_8 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
sound_9 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
sound_10 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_10')
sound_10.setVolume(1.0)
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)
sound_14 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_14')
sound_14.setVolume(1.0)
sound_15 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_15')
sound_15.setVolume(1.0)
sound_16 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_16')
sound_16.setVolume(1.0)
sound_17 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_17')
sound_17.setVolume(1.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Please alternate hand signal after each beep.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
sound_1 = sound.Sound('Thats-All-Folks.wav', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text="That's the end of the experiment. Thank you!",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "load_triggers"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
load_triggersComponents = []
for thisComponent in load_triggersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
load_triggersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "load_triggers"-------
while continueRoutine:
    # get current time
    t = load_triggersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=load_triggersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in load_triggersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "load_triggers"-------
for thisComponent in load_triggersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "load_triggers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
next.keys = []
next.rt = []
_next_allKeys = []
# keep track of which components have finished
trialComponents = [intro, next]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro* updates
    if intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro.frameNStart = frameN  # exact frame index
        intro.tStart = t  # local t and not account for scr refresh
        intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro, 'tStartRefresh')  # time at next scr refresh
        intro.setAutoDraw(True)
    
    # *next* updates
    waitOnFlip = False
    if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next.frameNStart = frameN  # exact frame index
        next.tStart = t  # local t and not account for scr refresh
        next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
        next.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next.status == STARTED and not waitOnFlip:
        theseKeys = next.getKeys(keyList=['space'], waitRelease=False)
        _next_allKeys.extend(theseKeys)
        if len(_next_allKeys):
            next.keys = _next_allKeys[-1].name  # just the last key pressed
            next.rt = _next_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro.started', intro.tStartRefresh)
thisExp.addData('intro.stopped', intro.tStopRefresh)
# check responses
if next.keys in ['', [], None]:  # No response was made
    next.keys = None
thisExp.addData('next.keys',next.keys)
if next.keys != None:  # we had a response
    thisExp.addData('next.rt', next.rt)
thisExp.addData('next.started', next.tStartRefresh)
thisExp.addData('next.stopped', next.tStopRefresh)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "baseline"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('baseline.wav', hamming=True)
    sound_2.setVolume(1.0, log=False)
    outlet.push_sample(x=[3])
    # keep track of which components have finished
    baselineComponents = [text, sound_2]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    outlet.push_sample(x=[3])
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simple_nonsync"-------
    continueRoutine = True
    # update component parameters for each repeat
    start_sound.setSound('simple_nonsync.wav', hamming=True)
    start_sound.setVolume(1.0, log=False)
    # keep track of which components have finished
    simple_nonsyncComponents = [start_sound, text_2]
    for thisComponent in simple_nonsyncComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    simple_nonsyncClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "simple_nonsync"-------
    while continueRoutine:
        # get current time
        t = simple_nonsyncClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=simple_nonsyncClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop start_sound
        if start_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_sound.frameNStart = frameN  # exact frame index
            start_sound.tStart = t  # local t and not account for scr refresh
            start_sound.tStartRefresh = tThisFlipGlobal  # on global time
            start_sound.play(when=win)  # sync with win flip
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simple_nonsyncComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simple_nonsync"-------
    for thisComponent in simple_nonsyncComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    start_sound.stop()  # ensure sound has stopped at end of routine
    trials.addData('start_sound.started', start_sound.tStartRefresh)
    trials.addData('start_sound.stopped', start_sound.tStopRefresh)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "simple_nonsync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simple_timing"-------
    continueRoutine = True
    routineTimer.add(90.250000)
    # update component parameters for each repeat
    sound_8.setSound('A', secs=0.25, hamming=True)
    sound_8.setVolume(1.0, log=False)
    sound_9.setSound('A', secs=0.25, hamming=True)
    sound_9.setVolume(1.0, log=False)
    sound_10.setSound('A', secs=0.25, hamming=True)
    sound_10.setVolume(1.0, log=False)
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=0.25, hamming=True)
    sound_13.setVolume(1.0, log=False)
    sound_14.setSound('A', secs=0.25, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_15.setSound('A', secs=0.25, hamming=True)
    sound_15.setVolume(1.0, log=False)
    sound_16.setSound('A', secs=0.25, hamming=True)
    sound_16.setVolume(1.0, log=False)
    sound_17.setSound('A', secs=0.25, hamming=True)
    sound_17.setVolume(1.0, log=False)
    outlet.push_sample(x=[1])
    # keep track of which components have finished
    simple_timingComponents = [sound_8, sound_9, sound_10, sound_11, sound_12, sound_13, sound_14, sound_15, sound_16, sound_17, text_9]
    for thisComponent in simple_timingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    simple_timingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "simple_timing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = simple_timingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=simple_timingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play(when=win)  # sync with win flip
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play(when=win)  # sync with win flip
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        # start/stop sound_10
        if sound_10.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.tStart = t  # local t and not account for scr refresh
            sound_10.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10.play(when=win)  # sync with win flip
        if sound_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_10.tStop = t  # not accounting for scr refresh
                sound_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10, 'tStopRefresh')  # time at next scr refresh
                sound_10.stop()
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        # start/stop sound_14
        if sound_14.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14.play(when=win)  # sync with win flip
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14, 'tStopRefresh')  # time at next scr refresh
                sound_14.stop()
        # start/stop sound_15
        if sound_15.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
            # keep track of start time/frame for later
            sound_15.frameNStart = frameN  # exact frame index
            sound_15.tStart = t  # local t and not account for scr refresh
            sound_15.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15.play(when=win)  # sync with win flip
        if sound_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_15.tStop = t  # not accounting for scr refresh
                sound_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15, 'tStopRefresh')  # time at next scr refresh
                sound_15.stop()
        # start/stop sound_16
        if sound_16.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            sound_16.frameNStart = frameN  # exact frame index
            sound_16.tStart = t  # local t and not account for scr refresh
            sound_16.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16.play(when=win)  # sync with win flip
        if sound_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_16.tStop = t  # not accounting for scr refresh
                sound_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16, 'tStopRefresh')  # time at next scr refresh
                sound_16.stop()
        # start/stop sound_17
        if sound_17.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            sound_17.frameNStart = frameN  # exact frame index
            sound_17.tStart = t  # local t and not account for scr refresh
            sound_17.tStartRefresh = tThisFlipGlobal  # on global time
            sound_17.play(when=win)  # sync with win flip
        if sound_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_17.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_17.tStop = t  # not accounting for scr refresh
                sound_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_17, 'tStopRefresh')  # time at next scr refresh
                sound_17.stop()
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 90-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simple_timingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simple_timing"-------
    for thisComponent in simple_timingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_8.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_8.started', sound_8.tStartRefresh)
    trials.addData('sound_8.stopped', sound_8.tStopRefresh)
    sound_9.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_9.started', sound_9.tStartRefresh)
    trials.addData('sound_9.stopped', sound_9.tStopRefresh)
    sound_10.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_10.started', sound_10.tStartRefresh)
    trials.addData('sound_10.stopped', sound_10.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_11.started', sound_11.tStartRefresh)
    trials.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_12.started', sound_12.tStartRefresh)
    trials.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_13.started', sound_13.tStartRefresh)
    trials.addData('sound_13.stopped', sound_13.tStopRefresh)
    sound_14.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_14.started', sound_14.tStartRefresh)
    trials.addData('sound_14.stopped', sound_14.tStopRefresh)
    sound_15.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_15.started', sound_15.tStartRefresh)
    trials.addData('sound_15.stopped', sound_15.tStopRefresh)
    sound_16.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_16.started', sound_16.tStartRefresh)
    trials.addData('sound_16.stopped', sound_16.tStopRefresh)
    sound_17.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_17.started', sound_17.tStartRefresh)
    trials.addData('sound_17.stopped', sound_17.tStopRefresh)
    trials.addData('text_9.started', text_9.tStartRefresh)
    trials.addData('text_9.stopped', text_9.tStopRefresh)
    outlet.push_sample(x=[1])
    
    # ------Prepare to start Routine "baseline"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('baseline.wav', hamming=True)
    sound_2.setVolume(1.0, log=False)
    outlet.push_sample(x=[3])
    # keep track of which components have finished
    baselineComponents = [text, sound_2]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    outlet.push_sample(x=[3])
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "complex_nonsync"-------
    continueRoutine = True
    # update component parameters for each repeat
    start_sound_2.setSound('complex_nonsync.wav', hamming=True)
    start_sound_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    complex_nonsyncComponents = [start_sound_2, text_3]
    for thisComponent in complex_nonsyncComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    complex_nonsyncClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "complex_nonsync"-------
    while continueRoutine:
        # get current time
        t = complex_nonsyncClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=complex_nonsyncClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop start_sound_2
        if start_sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_sound_2.frameNStart = frameN  # exact frame index
            start_sound_2.tStart = t  # local t and not account for scr refresh
            start_sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            start_sound_2.play(when=win)  # sync with win flip
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in complex_nonsyncComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "complex_nonsync"-------
    for thisComponent in complex_nonsyncComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    start_sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('start_sound_2.started', start_sound_2.tStartRefresh)
    trials.addData('start_sound_2.stopped', start_sound_2.tStopRefresh)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "complex_nonsync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "complex_timing"-------
    continueRoutine = True
    routineTimer.add(90.250000)
    # update component parameters for each repeat
    sound_7.setSound('A', secs=0.25, hamming=True)
    sound_7.setVolume(1.0, log=False)
    sound_18.setSound('A', secs=0.25, hamming=True)
    sound_18.setVolume(1.0, log=False)
    sound_19.setSound('A', secs=0.25, hamming=True)
    sound_19.setVolume(1.0, log=False)
    sound_20.setSound('A', secs=0.25, hamming=True)
    sound_20.setVolume(1.0, log=False)
    sound_21.setSound('A', secs=0.25, hamming=True)
    sound_21.setVolume(1.0, log=False)
    sound_22.setSound('A', secs=0.25, hamming=True)
    sound_22.setVolume(1.0, log=False)
    sound_23.setSound('A', secs=0.25, hamming=True)
    sound_23.setVolume(1.0, log=False)
    sound_24.setSound('A', secs=0.25, hamming=True)
    sound_24.setVolume(1.0, log=False)
    sound_26.setSound('A', secs=0.25, hamming=True)
    sound_26.setVolume(1.0, log=False)
    sound_25.setSound('A', secs=0.25, hamming=True)
    sound_25.setVolume(1.0, log=False)
    sound_27.setSound('A', secs=0.25, hamming=True)
    sound_27.setVolume(1.0, log=False)
    sound_31.setSound('A', secs=0.25, hamming=True)
    sound_31.setVolume(1.0, log=False)
    sound_32.setSound('A', secs=0.25, hamming=True)
    sound_32.setVolume(1.0, log=False)
    sound_30.setSound('A', secs=0.25, hamming=True)
    sound_30.setVolume(1.0, log=False)
    sound_35.setSound('A', secs=0.25, hamming=True)
    sound_35.setVolume(1.0, log=False)
    sound_34.setSound('A', secs=0.25, hamming=True)
    sound_34.setVolume(1.0, log=False)
    sound_33.setSound('A', secs=0.25, hamming=True)
    sound_33.setVolume(1.0, log=False)
    sound_29.setSound('A', secs=0.25, hamming=True)
    sound_29.setVolume(1.0, log=False)
    sound_28.setSound('A', secs=0.25, hamming=True)
    sound_28.setVolume(1.0, log=False)
    outlet.push_sample(x=[2])
    # keep track of which components have finished
    complex_timingComponents = [sound_7, sound_18, sound_19, sound_20, sound_21, sound_22, sound_23, sound_24, sound_26, sound_25, sound_27, sound_31, sound_32, sound_30, sound_35, sound_34, sound_33, sound_29, sound_28, text_10]
    for thisComponent in complex_timingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    complex_timingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "complex_timing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = complex_timingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=complex_timingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play(when=win)  # sync with win flip
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        # start/stop sound_18
        if sound_18.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.tStart = t  # local t and not account for scr refresh
            sound_18.tStartRefresh = tThisFlipGlobal  # on global time
            sound_18.play(when=win)  # sync with win flip
        if sound_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_18.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_18.tStop = t  # not accounting for scr refresh
                sound_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_18, 'tStopRefresh')  # time at next scr refresh
                sound_18.stop()
        # start/stop sound_19
        if sound_19.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.tStart = t  # local t and not account for scr refresh
            sound_19.tStartRefresh = tThisFlipGlobal  # on global time
            sound_19.play(when=win)  # sync with win flip
        if sound_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_19.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_19.tStop = t  # not accounting for scr refresh
                sound_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_19, 'tStopRefresh')  # time at next scr refresh
                sound_19.stop()
        # start/stop sound_20
        if sound_20.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.tStart = t  # local t and not account for scr refresh
            sound_20.tStartRefresh = tThisFlipGlobal  # on global time
            sound_20.play(when=win)  # sync with win flip
        if sound_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_20.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_20.tStop = t  # not accounting for scr refresh
                sound_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_20, 'tStopRefresh')  # time at next scr refresh
                sound_20.stop()
        # start/stop sound_21
        if sound_21.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.tStart = t  # local t and not account for scr refresh
            sound_21.tStartRefresh = tThisFlipGlobal  # on global time
            sound_21.play(when=win)  # sync with win flip
        if sound_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_21.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_21.tStop = t  # not accounting for scr refresh
                sound_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_21, 'tStopRefresh')  # time at next scr refresh
                sound_21.stop()
        # start/stop sound_22
        if sound_22.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            sound_22.frameNStart = frameN  # exact frame index
            sound_22.tStart = t  # local t and not account for scr refresh
            sound_22.tStartRefresh = tThisFlipGlobal  # on global time
            sound_22.play(when=win)  # sync with win flip
        if sound_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_22.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_22.tStop = t  # not accounting for scr refresh
                sound_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_22, 'tStopRefresh')  # time at next scr refresh
                sound_22.stop()
        # start/stop sound_23
        if sound_23.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            sound_23.frameNStart = frameN  # exact frame index
            sound_23.tStart = t  # local t and not account for scr refresh
            sound_23.tStartRefresh = tThisFlipGlobal  # on global time
            sound_23.play(when=win)  # sync with win flip
        if sound_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_23.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_23.tStop = t  # not accounting for scr refresh
                sound_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_23, 'tStopRefresh')  # time at next scr refresh
                sound_23.stop()
        # start/stop sound_24
        if sound_24.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
            # keep track of start time/frame for later
            sound_24.frameNStart = frameN  # exact frame index
            sound_24.tStart = t  # local t and not account for scr refresh
            sound_24.tStartRefresh = tThisFlipGlobal  # on global time
            sound_24.play(when=win)  # sync with win flip
        if sound_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_24.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_24.tStop = t  # not accounting for scr refresh
                sound_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_24, 'tStopRefresh')  # time at next scr refresh
                sound_24.stop()
        # start/stop sound_26
        if sound_26.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
            # keep track of start time/frame for later
            sound_26.frameNStart = frameN  # exact frame index
            sound_26.tStart = t  # local t and not account for scr refresh
            sound_26.tStartRefresh = tThisFlipGlobal  # on global time
            sound_26.play(when=win)  # sync with win flip
        if sound_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_26.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_26.tStop = t  # not accounting for scr refresh
                sound_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_26, 'tStopRefresh')  # time at next scr refresh
                sound_26.stop()
        # start/stop sound_25
        if sound_25.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
            # keep track of start time/frame for later
            sound_25.frameNStart = frameN  # exact frame index
            sound_25.tStart = t  # local t and not account for scr refresh
            sound_25.tStartRefresh = tThisFlipGlobal  # on global time
            sound_25.play(when=win)  # sync with win flip
        if sound_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_25.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_25.tStop = t  # not accounting for scr refresh
                sound_25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_25, 'tStopRefresh')  # time at next scr refresh
                sound_25.stop()
        # start/stop sound_27
        if sound_27.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            sound_27.frameNStart = frameN  # exact frame index
            sound_27.tStart = t  # local t and not account for scr refresh
            sound_27.tStartRefresh = tThisFlipGlobal  # on global time
            sound_27.play(when=win)  # sync with win flip
        if sound_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_27.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_27.tStop = t  # not accounting for scr refresh
                sound_27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_27, 'tStopRefresh')  # time at next scr refresh
                sound_27.stop()
        # start/stop sound_31
        if sound_31.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            sound_31.frameNStart = frameN  # exact frame index
            sound_31.tStart = t  # local t and not account for scr refresh
            sound_31.tStartRefresh = tThisFlipGlobal  # on global time
            sound_31.play(when=win)  # sync with win flip
        if sound_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_31.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_31.tStop = t  # not accounting for scr refresh
                sound_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_31, 'tStopRefresh')  # time at next scr refresh
                sound_31.stop()
        # start/stop sound_32
        if sound_32.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            sound_32.frameNStart = frameN  # exact frame index
            sound_32.tStart = t  # local t and not account for scr refresh
            sound_32.tStartRefresh = tThisFlipGlobal  # on global time
            sound_32.play(when=win)  # sync with win flip
        if sound_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_32.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_32.tStop = t  # not accounting for scr refresh
                sound_32.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_32, 'tStopRefresh')  # time at next scr refresh
                sound_32.stop()
        # start/stop sound_30
        if sound_30.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
            # keep track of start time/frame for later
            sound_30.frameNStart = frameN  # exact frame index
            sound_30.tStart = t  # local t and not account for scr refresh
            sound_30.tStartRefresh = tThisFlipGlobal  # on global time
            sound_30.play(when=win)  # sync with win flip
        if sound_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_30.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_30.tStop = t  # not accounting for scr refresh
                sound_30.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_30, 'tStopRefresh')  # time at next scr refresh
                sound_30.stop()
        # start/stop sound_35
        if sound_35.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
            # keep track of start time/frame for later
            sound_35.frameNStart = frameN  # exact frame index
            sound_35.tStart = t  # local t and not account for scr refresh
            sound_35.tStartRefresh = tThisFlipGlobal  # on global time
            sound_35.play(when=win)  # sync with win flip
        if sound_35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_35.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_35.tStop = t  # not accounting for scr refresh
                sound_35.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_35, 'tStopRefresh')  # time at next scr refresh
                sound_35.stop()
        # start/stop sound_34
        if sound_34.status == NOT_STARTED and tThisFlip >= 75-frameTolerance:
            # keep track of start time/frame for later
            sound_34.frameNStart = frameN  # exact frame index
            sound_34.tStart = t  # local t and not account for scr refresh
            sound_34.tStartRefresh = tThisFlipGlobal  # on global time
            sound_34.play(when=win)  # sync with win flip
        if sound_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_34.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_34.tStop = t  # not accounting for scr refresh
                sound_34.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_34, 'tStopRefresh')  # time at next scr refresh
                sound_34.stop()
        # start/stop sound_33
        if sound_33.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            sound_33.frameNStart = frameN  # exact frame index
            sound_33.tStart = t  # local t and not account for scr refresh
            sound_33.tStartRefresh = tThisFlipGlobal  # on global time
            sound_33.play(when=win)  # sync with win flip
        if sound_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_33.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_33.tStop = t  # not accounting for scr refresh
                sound_33.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_33, 'tStopRefresh')  # time at next scr refresh
                sound_33.stop()
        # start/stop sound_29
        if sound_29.status == NOT_STARTED and tThisFlip >= 85-frameTolerance:
            # keep track of start time/frame for later
            sound_29.frameNStart = frameN  # exact frame index
            sound_29.tStart = t  # local t and not account for scr refresh
            sound_29.tStartRefresh = tThisFlipGlobal  # on global time
            sound_29.play(when=win)  # sync with win flip
        if sound_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_29.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_29.tStop = t  # not accounting for scr refresh
                sound_29.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_29, 'tStopRefresh')  # time at next scr refresh
                sound_29.stop()
        # start/stop sound_28
        if sound_28.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            sound_28.frameNStart = frameN  # exact frame index
            sound_28.tStart = t  # local t and not account for scr refresh
            sound_28.tStartRefresh = tThisFlipGlobal  # on global time
            sound_28.play(when=win)  # sync with win flip
        if sound_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_28.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_28.tStop = t  # not accounting for scr refresh
                sound_28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_28, 'tStopRefresh')  # time at next scr refresh
                sound_28.stop()
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 90-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in complex_timingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "complex_timing"-------
    for thisComponent in complex_timingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_7.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_7.started', sound_7.tStartRefresh)
    trials.addData('sound_7.stopped', sound_7.tStopRefresh)
    sound_18.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_18.started', sound_18.tStartRefresh)
    trials.addData('sound_18.stopped', sound_18.tStopRefresh)
    sound_19.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_19.started', sound_19.tStartRefresh)
    trials.addData('sound_19.stopped', sound_19.tStopRefresh)
    sound_20.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_20.started', sound_20.tStartRefresh)
    trials.addData('sound_20.stopped', sound_20.tStopRefresh)
    sound_21.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_21.started', sound_21.tStartRefresh)
    trials.addData('sound_21.stopped', sound_21.tStopRefresh)
    sound_22.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_22.started', sound_22.tStartRefresh)
    trials.addData('sound_22.stopped', sound_22.tStopRefresh)
    sound_23.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_23.started', sound_23.tStartRefresh)
    trials.addData('sound_23.stopped', sound_23.tStopRefresh)
    sound_24.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_24.started', sound_24.tStartRefresh)
    trials.addData('sound_24.stopped', sound_24.tStopRefresh)
    sound_26.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_26.started', sound_26.tStartRefresh)
    trials.addData('sound_26.stopped', sound_26.tStopRefresh)
    sound_25.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_25.started', sound_25.tStartRefresh)
    trials.addData('sound_25.stopped', sound_25.tStopRefresh)
    sound_27.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_27.started', sound_27.tStartRefresh)
    trials.addData('sound_27.stopped', sound_27.tStopRefresh)
    sound_31.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_31.started', sound_31.tStartRefresh)
    trials.addData('sound_31.stopped', sound_31.tStopRefresh)
    sound_32.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_32.started', sound_32.tStartRefresh)
    trials.addData('sound_32.stopped', sound_32.tStopRefresh)
    sound_30.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_30.started', sound_30.tStartRefresh)
    trials.addData('sound_30.stopped', sound_30.tStopRefresh)
    sound_35.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_35.started', sound_35.tStartRefresh)
    trials.addData('sound_35.stopped', sound_35.tStopRefresh)
    sound_34.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_34.started', sound_34.tStartRefresh)
    trials.addData('sound_34.stopped', sound_34.tStopRefresh)
    sound_33.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_33.started', sound_33.tStartRefresh)
    trials.addData('sound_33.stopped', sound_33.tStopRefresh)
    sound_29.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_29.started', sound_29.tStartRefresh)
    trials.addData('sound_29.stopped', sound_29.tStopRefresh)
    sound_28.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_28.started', sound_28.tStartRefresh)
    trials.addData('sound_28.stopped', sound_28.tStopRefresh)
    trials.addData('text_10.started', text_10.tStartRefresh)
    trials.addData('text_10.stopped', text_10.tStopRefresh)
    outlet.push_sample(x=[2])
    
    # ------Prepare to start Routine "baseline"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('baseline.wav', hamming=True)
    sound_2.setVolume(1.0, log=False)
    outlet.push_sample(x=[3])
    # keep track of which components have finished
    baselineComponents = [text, sound_2]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    outlet.push_sample(x=[3])
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sync_complex_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_3.setSound('sync_complex_A.wav', hamming=True)
    sound_3.setVolume(1.0, log=False)
    # keep track of which components have finished
    sync_complex_AComponents = [text_4, sound_3]
    for thisComponent in sync_complex_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sync_complex_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sync_complex_A"-------
    while continueRoutine:
        # get current time
        t = sync_complex_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sync_complex_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sync_complex_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sync_complex_A"-------
    for thisComponent in sync_complex_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    sound_3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_3.started', sound_3.tStartRefresh)
    trials.addData('sound_3.stopped', sound_3.tStopRefresh)
    # the Routine "sync_complex_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "complex_timing"-------
    continueRoutine = True
    routineTimer.add(90.250000)
    # update component parameters for each repeat
    sound_7.setSound('A', secs=0.25, hamming=True)
    sound_7.setVolume(1.0, log=False)
    sound_18.setSound('A', secs=0.25, hamming=True)
    sound_18.setVolume(1.0, log=False)
    sound_19.setSound('A', secs=0.25, hamming=True)
    sound_19.setVolume(1.0, log=False)
    sound_20.setSound('A', secs=0.25, hamming=True)
    sound_20.setVolume(1.0, log=False)
    sound_21.setSound('A', secs=0.25, hamming=True)
    sound_21.setVolume(1.0, log=False)
    sound_22.setSound('A', secs=0.25, hamming=True)
    sound_22.setVolume(1.0, log=False)
    sound_23.setSound('A', secs=0.25, hamming=True)
    sound_23.setVolume(1.0, log=False)
    sound_24.setSound('A', secs=0.25, hamming=True)
    sound_24.setVolume(1.0, log=False)
    sound_26.setSound('A', secs=0.25, hamming=True)
    sound_26.setVolume(1.0, log=False)
    sound_25.setSound('A', secs=0.25, hamming=True)
    sound_25.setVolume(1.0, log=False)
    sound_27.setSound('A', secs=0.25, hamming=True)
    sound_27.setVolume(1.0, log=False)
    sound_31.setSound('A', secs=0.25, hamming=True)
    sound_31.setVolume(1.0, log=False)
    sound_32.setSound('A', secs=0.25, hamming=True)
    sound_32.setVolume(1.0, log=False)
    sound_30.setSound('A', secs=0.25, hamming=True)
    sound_30.setVolume(1.0, log=False)
    sound_35.setSound('A', secs=0.25, hamming=True)
    sound_35.setVolume(1.0, log=False)
    sound_34.setSound('A', secs=0.25, hamming=True)
    sound_34.setVolume(1.0, log=False)
    sound_33.setSound('A', secs=0.25, hamming=True)
    sound_33.setVolume(1.0, log=False)
    sound_29.setSound('A', secs=0.25, hamming=True)
    sound_29.setVolume(1.0, log=False)
    sound_28.setSound('A', secs=0.25, hamming=True)
    sound_28.setVolume(1.0, log=False)
    outlet.push_sample(x=[2])
    # keep track of which components have finished
    complex_timingComponents = [sound_7, sound_18, sound_19, sound_20, sound_21, sound_22, sound_23, sound_24, sound_26, sound_25, sound_27, sound_31, sound_32, sound_30, sound_35, sound_34, sound_33, sound_29, sound_28, text_10]
    for thisComponent in complex_timingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    complex_timingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "complex_timing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = complex_timingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=complex_timingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play(when=win)  # sync with win flip
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        # start/stop sound_18
        if sound_18.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.tStart = t  # local t and not account for scr refresh
            sound_18.tStartRefresh = tThisFlipGlobal  # on global time
            sound_18.play(when=win)  # sync with win flip
        if sound_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_18.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_18.tStop = t  # not accounting for scr refresh
                sound_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_18, 'tStopRefresh')  # time at next scr refresh
                sound_18.stop()
        # start/stop sound_19
        if sound_19.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.tStart = t  # local t and not account for scr refresh
            sound_19.tStartRefresh = tThisFlipGlobal  # on global time
            sound_19.play(when=win)  # sync with win flip
        if sound_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_19.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_19.tStop = t  # not accounting for scr refresh
                sound_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_19, 'tStopRefresh')  # time at next scr refresh
                sound_19.stop()
        # start/stop sound_20
        if sound_20.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.tStart = t  # local t and not account for scr refresh
            sound_20.tStartRefresh = tThisFlipGlobal  # on global time
            sound_20.play(when=win)  # sync with win flip
        if sound_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_20.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_20.tStop = t  # not accounting for scr refresh
                sound_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_20, 'tStopRefresh')  # time at next scr refresh
                sound_20.stop()
        # start/stop sound_21
        if sound_21.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.tStart = t  # local t and not account for scr refresh
            sound_21.tStartRefresh = tThisFlipGlobal  # on global time
            sound_21.play(when=win)  # sync with win flip
        if sound_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_21.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_21.tStop = t  # not accounting for scr refresh
                sound_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_21, 'tStopRefresh')  # time at next scr refresh
                sound_21.stop()
        # start/stop sound_22
        if sound_22.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            sound_22.frameNStart = frameN  # exact frame index
            sound_22.tStart = t  # local t and not account for scr refresh
            sound_22.tStartRefresh = tThisFlipGlobal  # on global time
            sound_22.play(when=win)  # sync with win flip
        if sound_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_22.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_22.tStop = t  # not accounting for scr refresh
                sound_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_22, 'tStopRefresh')  # time at next scr refresh
                sound_22.stop()
        # start/stop sound_23
        if sound_23.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            sound_23.frameNStart = frameN  # exact frame index
            sound_23.tStart = t  # local t and not account for scr refresh
            sound_23.tStartRefresh = tThisFlipGlobal  # on global time
            sound_23.play(when=win)  # sync with win flip
        if sound_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_23.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_23.tStop = t  # not accounting for scr refresh
                sound_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_23, 'tStopRefresh')  # time at next scr refresh
                sound_23.stop()
        # start/stop sound_24
        if sound_24.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
            # keep track of start time/frame for later
            sound_24.frameNStart = frameN  # exact frame index
            sound_24.tStart = t  # local t and not account for scr refresh
            sound_24.tStartRefresh = tThisFlipGlobal  # on global time
            sound_24.play(when=win)  # sync with win flip
        if sound_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_24.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_24.tStop = t  # not accounting for scr refresh
                sound_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_24, 'tStopRefresh')  # time at next scr refresh
                sound_24.stop()
        # start/stop sound_26
        if sound_26.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
            # keep track of start time/frame for later
            sound_26.frameNStart = frameN  # exact frame index
            sound_26.tStart = t  # local t and not account for scr refresh
            sound_26.tStartRefresh = tThisFlipGlobal  # on global time
            sound_26.play(when=win)  # sync with win flip
        if sound_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_26.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_26.tStop = t  # not accounting for scr refresh
                sound_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_26, 'tStopRefresh')  # time at next scr refresh
                sound_26.stop()
        # start/stop sound_25
        if sound_25.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
            # keep track of start time/frame for later
            sound_25.frameNStart = frameN  # exact frame index
            sound_25.tStart = t  # local t and not account for scr refresh
            sound_25.tStartRefresh = tThisFlipGlobal  # on global time
            sound_25.play(when=win)  # sync with win flip
        if sound_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_25.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_25.tStop = t  # not accounting for scr refresh
                sound_25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_25, 'tStopRefresh')  # time at next scr refresh
                sound_25.stop()
        # start/stop sound_27
        if sound_27.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            sound_27.frameNStart = frameN  # exact frame index
            sound_27.tStart = t  # local t and not account for scr refresh
            sound_27.tStartRefresh = tThisFlipGlobal  # on global time
            sound_27.play(when=win)  # sync with win flip
        if sound_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_27.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_27.tStop = t  # not accounting for scr refresh
                sound_27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_27, 'tStopRefresh')  # time at next scr refresh
                sound_27.stop()
        # start/stop sound_31
        if sound_31.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            sound_31.frameNStart = frameN  # exact frame index
            sound_31.tStart = t  # local t and not account for scr refresh
            sound_31.tStartRefresh = tThisFlipGlobal  # on global time
            sound_31.play(when=win)  # sync with win flip
        if sound_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_31.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_31.tStop = t  # not accounting for scr refresh
                sound_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_31, 'tStopRefresh')  # time at next scr refresh
                sound_31.stop()
        # start/stop sound_32
        if sound_32.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            sound_32.frameNStart = frameN  # exact frame index
            sound_32.tStart = t  # local t and not account for scr refresh
            sound_32.tStartRefresh = tThisFlipGlobal  # on global time
            sound_32.play(when=win)  # sync with win flip
        if sound_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_32.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_32.tStop = t  # not accounting for scr refresh
                sound_32.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_32, 'tStopRefresh')  # time at next scr refresh
                sound_32.stop()
        # start/stop sound_30
        if sound_30.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
            # keep track of start time/frame for later
            sound_30.frameNStart = frameN  # exact frame index
            sound_30.tStart = t  # local t and not account for scr refresh
            sound_30.tStartRefresh = tThisFlipGlobal  # on global time
            sound_30.play(when=win)  # sync with win flip
        if sound_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_30.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_30.tStop = t  # not accounting for scr refresh
                sound_30.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_30, 'tStopRefresh')  # time at next scr refresh
                sound_30.stop()
        # start/stop sound_35
        if sound_35.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
            # keep track of start time/frame for later
            sound_35.frameNStart = frameN  # exact frame index
            sound_35.tStart = t  # local t and not account for scr refresh
            sound_35.tStartRefresh = tThisFlipGlobal  # on global time
            sound_35.play(when=win)  # sync with win flip
        if sound_35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_35.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_35.tStop = t  # not accounting for scr refresh
                sound_35.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_35, 'tStopRefresh')  # time at next scr refresh
                sound_35.stop()
        # start/stop sound_34
        if sound_34.status == NOT_STARTED and tThisFlip >= 75-frameTolerance:
            # keep track of start time/frame for later
            sound_34.frameNStart = frameN  # exact frame index
            sound_34.tStart = t  # local t and not account for scr refresh
            sound_34.tStartRefresh = tThisFlipGlobal  # on global time
            sound_34.play(when=win)  # sync with win flip
        if sound_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_34.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_34.tStop = t  # not accounting for scr refresh
                sound_34.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_34, 'tStopRefresh')  # time at next scr refresh
                sound_34.stop()
        # start/stop sound_33
        if sound_33.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            sound_33.frameNStart = frameN  # exact frame index
            sound_33.tStart = t  # local t and not account for scr refresh
            sound_33.tStartRefresh = tThisFlipGlobal  # on global time
            sound_33.play(when=win)  # sync with win flip
        if sound_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_33.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_33.tStop = t  # not accounting for scr refresh
                sound_33.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_33, 'tStopRefresh')  # time at next scr refresh
                sound_33.stop()
        # start/stop sound_29
        if sound_29.status == NOT_STARTED and tThisFlip >= 85-frameTolerance:
            # keep track of start time/frame for later
            sound_29.frameNStart = frameN  # exact frame index
            sound_29.tStart = t  # local t and not account for scr refresh
            sound_29.tStartRefresh = tThisFlipGlobal  # on global time
            sound_29.play(when=win)  # sync with win flip
        if sound_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_29.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_29.tStop = t  # not accounting for scr refresh
                sound_29.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_29, 'tStopRefresh')  # time at next scr refresh
                sound_29.stop()
        # start/stop sound_28
        if sound_28.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            sound_28.frameNStart = frameN  # exact frame index
            sound_28.tStart = t  # local t and not account for scr refresh
            sound_28.tStartRefresh = tThisFlipGlobal  # on global time
            sound_28.play(when=win)  # sync with win flip
        if sound_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_28.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_28.tStop = t  # not accounting for scr refresh
                sound_28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_28, 'tStopRefresh')  # time at next scr refresh
                sound_28.stop()
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 90-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in complex_timingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "complex_timing"-------
    for thisComponent in complex_timingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_7.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_7.started', sound_7.tStartRefresh)
    trials.addData('sound_7.stopped', sound_7.tStopRefresh)
    sound_18.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_18.started', sound_18.tStartRefresh)
    trials.addData('sound_18.stopped', sound_18.tStopRefresh)
    sound_19.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_19.started', sound_19.tStartRefresh)
    trials.addData('sound_19.stopped', sound_19.tStopRefresh)
    sound_20.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_20.started', sound_20.tStartRefresh)
    trials.addData('sound_20.stopped', sound_20.tStopRefresh)
    sound_21.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_21.started', sound_21.tStartRefresh)
    trials.addData('sound_21.stopped', sound_21.tStopRefresh)
    sound_22.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_22.started', sound_22.tStartRefresh)
    trials.addData('sound_22.stopped', sound_22.tStopRefresh)
    sound_23.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_23.started', sound_23.tStartRefresh)
    trials.addData('sound_23.stopped', sound_23.tStopRefresh)
    sound_24.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_24.started', sound_24.tStartRefresh)
    trials.addData('sound_24.stopped', sound_24.tStopRefresh)
    sound_26.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_26.started', sound_26.tStartRefresh)
    trials.addData('sound_26.stopped', sound_26.tStopRefresh)
    sound_25.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_25.started', sound_25.tStartRefresh)
    trials.addData('sound_25.stopped', sound_25.tStopRefresh)
    sound_27.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_27.started', sound_27.tStartRefresh)
    trials.addData('sound_27.stopped', sound_27.tStopRefresh)
    sound_31.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_31.started', sound_31.tStartRefresh)
    trials.addData('sound_31.stopped', sound_31.tStopRefresh)
    sound_32.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_32.started', sound_32.tStartRefresh)
    trials.addData('sound_32.stopped', sound_32.tStopRefresh)
    sound_30.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_30.started', sound_30.tStartRefresh)
    trials.addData('sound_30.stopped', sound_30.tStopRefresh)
    sound_35.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_35.started', sound_35.tStartRefresh)
    trials.addData('sound_35.stopped', sound_35.tStopRefresh)
    sound_34.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_34.started', sound_34.tStartRefresh)
    trials.addData('sound_34.stopped', sound_34.tStopRefresh)
    sound_33.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_33.started', sound_33.tStartRefresh)
    trials.addData('sound_33.stopped', sound_33.tStopRefresh)
    sound_29.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_29.started', sound_29.tStartRefresh)
    trials.addData('sound_29.stopped', sound_29.tStopRefresh)
    sound_28.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_28.started', sound_28.tStartRefresh)
    trials.addData('sound_28.stopped', sound_28.tStopRefresh)
    trials.addData('text_10.started', text_10.tStartRefresh)
    trials.addData('text_10.stopped', text_10.tStopRefresh)
    outlet.push_sample(x=[2])
    
    # ------Prepare to start Routine "baseline"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('baseline.wav', hamming=True)
    sound_2.setVolume(1.0, log=False)
    outlet.push_sample(x=[3])
    # keep track of which components have finished
    baselineComponents = [text, sound_2]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    outlet.push_sample(x=[3])
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sync_complex_b"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_4.setSound('sync_complex_B.wav', hamming=True)
    sound_4.setVolume(1.0, log=False)
    # keep track of which components have finished
    sync_complex_bComponents = [text_5, sound_4]
    for thisComponent in sync_complex_bComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sync_complex_bClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sync_complex_b"-------
    while continueRoutine:
        # get current time
        t = sync_complex_bClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sync_complex_bClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        # start/stop sound_4
        if sound_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.tStart = t  # local t and not account for scr refresh
            sound_4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sync_complex_bComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sync_complex_b"-------
    for thisComponent in sync_complex_bComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    sound_4.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_4.started', sound_4.tStartRefresh)
    trials.addData('sound_4.stopped', sound_4.tStopRefresh)
    # the Routine "sync_complex_b" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "complex_timing"-------
    continueRoutine = True
    routineTimer.add(90.250000)
    # update component parameters for each repeat
    sound_7.setSound('A', secs=0.25, hamming=True)
    sound_7.setVolume(1.0, log=False)
    sound_18.setSound('A', secs=0.25, hamming=True)
    sound_18.setVolume(1.0, log=False)
    sound_19.setSound('A', secs=0.25, hamming=True)
    sound_19.setVolume(1.0, log=False)
    sound_20.setSound('A', secs=0.25, hamming=True)
    sound_20.setVolume(1.0, log=False)
    sound_21.setSound('A', secs=0.25, hamming=True)
    sound_21.setVolume(1.0, log=False)
    sound_22.setSound('A', secs=0.25, hamming=True)
    sound_22.setVolume(1.0, log=False)
    sound_23.setSound('A', secs=0.25, hamming=True)
    sound_23.setVolume(1.0, log=False)
    sound_24.setSound('A', secs=0.25, hamming=True)
    sound_24.setVolume(1.0, log=False)
    sound_26.setSound('A', secs=0.25, hamming=True)
    sound_26.setVolume(1.0, log=False)
    sound_25.setSound('A', secs=0.25, hamming=True)
    sound_25.setVolume(1.0, log=False)
    sound_27.setSound('A', secs=0.25, hamming=True)
    sound_27.setVolume(1.0, log=False)
    sound_31.setSound('A', secs=0.25, hamming=True)
    sound_31.setVolume(1.0, log=False)
    sound_32.setSound('A', secs=0.25, hamming=True)
    sound_32.setVolume(1.0, log=False)
    sound_30.setSound('A', secs=0.25, hamming=True)
    sound_30.setVolume(1.0, log=False)
    sound_35.setSound('A', secs=0.25, hamming=True)
    sound_35.setVolume(1.0, log=False)
    sound_34.setSound('A', secs=0.25, hamming=True)
    sound_34.setVolume(1.0, log=False)
    sound_33.setSound('A', secs=0.25, hamming=True)
    sound_33.setVolume(1.0, log=False)
    sound_29.setSound('A', secs=0.25, hamming=True)
    sound_29.setVolume(1.0, log=False)
    sound_28.setSound('A', secs=0.25, hamming=True)
    sound_28.setVolume(1.0, log=False)
    outlet.push_sample(x=[2])
    # keep track of which components have finished
    complex_timingComponents = [sound_7, sound_18, sound_19, sound_20, sound_21, sound_22, sound_23, sound_24, sound_26, sound_25, sound_27, sound_31, sound_32, sound_30, sound_35, sound_34, sound_33, sound_29, sound_28, text_10]
    for thisComponent in complex_timingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    complex_timingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "complex_timing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = complex_timingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=complex_timingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play(when=win)  # sync with win flip
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        # start/stop sound_18
        if sound_18.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.tStart = t  # local t and not account for scr refresh
            sound_18.tStartRefresh = tThisFlipGlobal  # on global time
            sound_18.play(when=win)  # sync with win flip
        if sound_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_18.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_18.tStop = t  # not accounting for scr refresh
                sound_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_18, 'tStopRefresh')  # time at next scr refresh
                sound_18.stop()
        # start/stop sound_19
        if sound_19.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.tStart = t  # local t and not account for scr refresh
            sound_19.tStartRefresh = tThisFlipGlobal  # on global time
            sound_19.play(when=win)  # sync with win flip
        if sound_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_19.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_19.tStop = t  # not accounting for scr refresh
                sound_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_19, 'tStopRefresh')  # time at next scr refresh
                sound_19.stop()
        # start/stop sound_20
        if sound_20.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.tStart = t  # local t and not account for scr refresh
            sound_20.tStartRefresh = tThisFlipGlobal  # on global time
            sound_20.play(when=win)  # sync with win flip
        if sound_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_20.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_20.tStop = t  # not accounting for scr refresh
                sound_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_20, 'tStopRefresh')  # time at next scr refresh
                sound_20.stop()
        # start/stop sound_21
        if sound_21.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.tStart = t  # local t and not account for scr refresh
            sound_21.tStartRefresh = tThisFlipGlobal  # on global time
            sound_21.play(when=win)  # sync with win flip
        if sound_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_21.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_21.tStop = t  # not accounting for scr refresh
                sound_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_21, 'tStopRefresh')  # time at next scr refresh
                sound_21.stop()
        # start/stop sound_22
        if sound_22.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            sound_22.frameNStart = frameN  # exact frame index
            sound_22.tStart = t  # local t and not account for scr refresh
            sound_22.tStartRefresh = tThisFlipGlobal  # on global time
            sound_22.play(when=win)  # sync with win flip
        if sound_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_22.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_22.tStop = t  # not accounting for scr refresh
                sound_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_22, 'tStopRefresh')  # time at next scr refresh
                sound_22.stop()
        # start/stop sound_23
        if sound_23.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            sound_23.frameNStart = frameN  # exact frame index
            sound_23.tStart = t  # local t and not account for scr refresh
            sound_23.tStartRefresh = tThisFlipGlobal  # on global time
            sound_23.play(when=win)  # sync with win flip
        if sound_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_23.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_23.tStop = t  # not accounting for scr refresh
                sound_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_23, 'tStopRefresh')  # time at next scr refresh
                sound_23.stop()
        # start/stop sound_24
        if sound_24.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
            # keep track of start time/frame for later
            sound_24.frameNStart = frameN  # exact frame index
            sound_24.tStart = t  # local t and not account for scr refresh
            sound_24.tStartRefresh = tThisFlipGlobal  # on global time
            sound_24.play(when=win)  # sync with win flip
        if sound_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_24.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_24.tStop = t  # not accounting for scr refresh
                sound_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_24, 'tStopRefresh')  # time at next scr refresh
                sound_24.stop()
        # start/stop sound_26
        if sound_26.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
            # keep track of start time/frame for later
            sound_26.frameNStart = frameN  # exact frame index
            sound_26.tStart = t  # local t and not account for scr refresh
            sound_26.tStartRefresh = tThisFlipGlobal  # on global time
            sound_26.play(when=win)  # sync with win flip
        if sound_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_26.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_26.tStop = t  # not accounting for scr refresh
                sound_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_26, 'tStopRefresh')  # time at next scr refresh
                sound_26.stop()
        # start/stop sound_25
        if sound_25.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
            # keep track of start time/frame for later
            sound_25.frameNStart = frameN  # exact frame index
            sound_25.tStart = t  # local t and not account for scr refresh
            sound_25.tStartRefresh = tThisFlipGlobal  # on global time
            sound_25.play(when=win)  # sync with win flip
        if sound_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_25.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_25.tStop = t  # not accounting for scr refresh
                sound_25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_25, 'tStopRefresh')  # time at next scr refresh
                sound_25.stop()
        # start/stop sound_27
        if sound_27.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            sound_27.frameNStart = frameN  # exact frame index
            sound_27.tStart = t  # local t and not account for scr refresh
            sound_27.tStartRefresh = tThisFlipGlobal  # on global time
            sound_27.play(when=win)  # sync with win flip
        if sound_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_27.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_27.tStop = t  # not accounting for scr refresh
                sound_27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_27, 'tStopRefresh')  # time at next scr refresh
                sound_27.stop()
        # start/stop sound_31
        if sound_31.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            sound_31.frameNStart = frameN  # exact frame index
            sound_31.tStart = t  # local t and not account for scr refresh
            sound_31.tStartRefresh = tThisFlipGlobal  # on global time
            sound_31.play(when=win)  # sync with win flip
        if sound_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_31.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_31.tStop = t  # not accounting for scr refresh
                sound_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_31, 'tStopRefresh')  # time at next scr refresh
                sound_31.stop()
        # start/stop sound_32
        if sound_32.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            sound_32.frameNStart = frameN  # exact frame index
            sound_32.tStart = t  # local t and not account for scr refresh
            sound_32.tStartRefresh = tThisFlipGlobal  # on global time
            sound_32.play(when=win)  # sync with win flip
        if sound_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_32.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_32.tStop = t  # not accounting for scr refresh
                sound_32.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_32, 'tStopRefresh')  # time at next scr refresh
                sound_32.stop()
        # start/stop sound_30
        if sound_30.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
            # keep track of start time/frame for later
            sound_30.frameNStart = frameN  # exact frame index
            sound_30.tStart = t  # local t and not account for scr refresh
            sound_30.tStartRefresh = tThisFlipGlobal  # on global time
            sound_30.play(when=win)  # sync with win flip
        if sound_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_30.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_30.tStop = t  # not accounting for scr refresh
                sound_30.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_30, 'tStopRefresh')  # time at next scr refresh
                sound_30.stop()
        # start/stop sound_35
        if sound_35.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
            # keep track of start time/frame for later
            sound_35.frameNStart = frameN  # exact frame index
            sound_35.tStart = t  # local t and not account for scr refresh
            sound_35.tStartRefresh = tThisFlipGlobal  # on global time
            sound_35.play(when=win)  # sync with win flip
        if sound_35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_35.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_35.tStop = t  # not accounting for scr refresh
                sound_35.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_35, 'tStopRefresh')  # time at next scr refresh
                sound_35.stop()
        # start/stop sound_34
        if sound_34.status == NOT_STARTED and tThisFlip >= 75-frameTolerance:
            # keep track of start time/frame for later
            sound_34.frameNStart = frameN  # exact frame index
            sound_34.tStart = t  # local t and not account for scr refresh
            sound_34.tStartRefresh = tThisFlipGlobal  # on global time
            sound_34.play(when=win)  # sync with win flip
        if sound_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_34.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_34.tStop = t  # not accounting for scr refresh
                sound_34.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_34, 'tStopRefresh')  # time at next scr refresh
                sound_34.stop()
        # start/stop sound_33
        if sound_33.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            sound_33.frameNStart = frameN  # exact frame index
            sound_33.tStart = t  # local t and not account for scr refresh
            sound_33.tStartRefresh = tThisFlipGlobal  # on global time
            sound_33.play(when=win)  # sync with win flip
        if sound_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_33.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_33.tStop = t  # not accounting for scr refresh
                sound_33.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_33, 'tStopRefresh')  # time at next scr refresh
                sound_33.stop()
        # start/stop sound_29
        if sound_29.status == NOT_STARTED and tThisFlip >= 85-frameTolerance:
            # keep track of start time/frame for later
            sound_29.frameNStart = frameN  # exact frame index
            sound_29.tStart = t  # local t and not account for scr refresh
            sound_29.tStartRefresh = tThisFlipGlobal  # on global time
            sound_29.play(when=win)  # sync with win flip
        if sound_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_29.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_29.tStop = t  # not accounting for scr refresh
                sound_29.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_29, 'tStopRefresh')  # time at next scr refresh
                sound_29.stop()
        # start/stop sound_28
        if sound_28.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            sound_28.frameNStart = frameN  # exact frame index
            sound_28.tStart = t  # local t and not account for scr refresh
            sound_28.tStartRefresh = tThisFlipGlobal  # on global time
            sound_28.play(when=win)  # sync with win flip
        if sound_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_28.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_28.tStop = t  # not accounting for scr refresh
                sound_28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_28, 'tStopRefresh')  # time at next scr refresh
                sound_28.stop()
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 90-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in complex_timingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "complex_timing"-------
    for thisComponent in complex_timingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_7.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_7.started', sound_7.tStartRefresh)
    trials.addData('sound_7.stopped', sound_7.tStopRefresh)
    sound_18.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_18.started', sound_18.tStartRefresh)
    trials.addData('sound_18.stopped', sound_18.tStopRefresh)
    sound_19.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_19.started', sound_19.tStartRefresh)
    trials.addData('sound_19.stopped', sound_19.tStopRefresh)
    sound_20.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_20.started', sound_20.tStartRefresh)
    trials.addData('sound_20.stopped', sound_20.tStopRefresh)
    sound_21.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_21.started', sound_21.tStartRefresh)
    trials.addData('sound_21.stopped', sound_21.tStopRefresh)
    sound_22.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_22.started', sound_22.tStartRefresh)
    trials.addData('sound_22.stopped', sound_22.tStopRefresh)
    sound_23.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_23.started', sound_23.tStartRefresh)
    trials.addData('sound_23.stopped', sound_23.tStopRefresh)
    sound_24.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_24.started', sound_24.tStartRefresh)
    trials.addData('sound_24.stopped', sound_24.tStopRefresh)
    sound_26.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_26.started', sound_26.tStartRefresh)
    trials.addData('sound_26.stopped', sound_26.tStopRefresh)
    sound_25.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_25.started', sound_25.tStartRefresh)
    trials.addData('sound_25.stopped', sound_25.tStopRefresh)
    sound_27.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_27.started', sound_27.tStartRefresh)
    trials.addData('sound_27.stopped', sound_27.tStopRefresh)
    sound_31.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_31.started', sound_31.tStartRefresh)
    trials.addData('sound_31.stopped', sound_31.tStopRefresh)
    sound_32.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_32.started', sound_32.tStartRefresh)
    trials.addData('sound_32.stopped', sound_32.tStopRefresh)
    sound_30.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_30.started', sound_30.tStartRefresh)
    trials.addData('sound_30.stopped', sound_30.tStopRefresh)
    sound_35.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_35.started', sound_35.tStartRefresh)
    trials.addData('sound_35.stopped', sound_35.tStopRefresh)
    sound_34.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_34.started', sound_34.tStartRefresh)
    trials.addData('sound_34.stopped', sound_34.tStopRefresh)
    sound_33.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_33.started', sound_33.tStartRefresh)
    trials.addData('sound_33.stopped', sound_33.tStopRefresh)
    sound_29.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_29.started', sound_29.tStartRefresh)
    trials.addData('sound_29.stopped', sound_29.tStopRefresh)
    sound_28.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_28.started', sound_28.tStartRefresh)
    trials.addData('sound_28.stopped', sound_28.tStopRefresh)
    trials.addData('text_10.started', text_10.tStartRefresh)
    trials.addData('text_10.stopped', text_10.tStopRefresh)
    outlet.push_sample(x=[2])
    
    # ------Prepare to start Routine "baseline"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('baseline.wav', hamming=True)
    sound_2.setVolume(1.0, log=False)
    outlet.push_sample(x=[3])
    # keep track of which components have finished
    baselineComponents = [text, sound_2]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    outlet.push_sample(x=[3])
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sync_simple_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_5.setSound('sync_simple_A.wav', hamming=True)
    sound_5.setVolume(1.0, log=False)
    # keep track of which components have finished
    sync_simple_AComponents = [text_7, sound_5]
    for thisComponent in sync_simple_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sync_simple_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sync_simple_A"-------
    while continueRoutine:
        # get current time
        t = sync_simple_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sync_simple_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        # start/stop sound_5
        if sound_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.tStart = t  # local t and not account for scr refresh
            sound_5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sync_simple_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sync_simple_A"-------
    for thisComponent in sync_simple_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_7.started', text_7.tStartRefresh)
    trials.addData('text_7.stopped', text_7.tStopRefresh)
    sound_5.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_5.started', sound_5.tStartRefresh)
    trials.addData('sound_5.stopped', sound_5.tStopRefresh)
    # the Routine "sync_simple_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simple_timing"-------
    continueRoutine = True
    routineTimer.add(90.250000)
    # update component parameters for each repeat
    sound_8.setSound('A', secs=0.25, hamming=True)
    sound_8.setVolume(1.0, log=False)
    sound_9.setSound('A', secs=0.25, hamming=True)
    sound_9.setVolume(1.0, log=False)
    sound_10.setSound('A', secs=0.25, hamming=True)
    sound_10.setVolume(1.0, log=False)
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=0.25, hamming=True)
    sound_13.setVolume(1.0, log=False)
    sound_14.setSound('A', secs=0.25, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_15.setSound('A', secs=0.25, hamming=True)
    sound_15.setVolume(1.0, log=False)
    sound_16.setSound('A', secs=0.25, hamming=True)
    sound_16.setVolume(1.0, log=False)
    sound_17.setSound('A', secs=0.25, hamming=True)
    sound_17.setVolume(1.0, log=False)
    outlet.push_sample(x=[1])
    # keep track of which components have finished
    simple_timingComponents = [sound_8, sound_9, sound_10, sound_11, sound_12, sound_13, sound_14, sound_15, sound_16, sound_17, text_9]
    for thisComponent in simple_timingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    simple_timingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "simple_timing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = simple_timingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=simple_timingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play(when=win)  # sync with win flip
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play(when=win)  # sync with win flip
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        # start/stop sound_10
        if sound_10.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.tStart = t  # local t and not account for scr refresh
            sound_10.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10.play(when=win)  # sync with win flip
        if sound_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_10.tStop = t  # not accounting for scr refresh
                sound_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10, 'tStopRefresh')  # time at next scr refresh
                sound_10.stop()
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        # start/stop sound_14
        if sound_14.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14.play(when=win)  # sync with win flip
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14, 'tStopRefresh')  # time at next scr refresh
                sound_14.stop()
        # start/stop sound_15
        if sound_15.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
            # keep track of start time/frame for later
            sound_15.frameNStart = frameN  # exact frame index
            sound_15.tStart = t  # local t and not account for scr refresh
            sound_15.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15.play(when=win)  # sync with win flip
        if sound_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_15.tStop = t  # not accounting for scr refresh
                sound_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15, 'tStopRefresh')  # time at next scr refresh
                sound_15.stop()
        # start/stop sound_16
        if sound_16.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            sound_16.frameNStart = frameN  # exact frame index
            sound_16.tStart = t  # local t and not account for scr refresh
            sound_16.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16.play(when=win)  # sync with win flip
        if sound_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_16.tStop = t  # not accounting for scr refresh
                sound_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16, 'tStopRefresh')  # time at next scr refresh
                sound_16.stop()
        # start/stop sound_17
        if sound_17.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            sound_17.frameNStart = frameN  # exact frame index
            sound_17.tStart = t  # local t and not account for scr refresh
            sound_17.tStartRefresh = tThisFlipGlobal  # on global time
            sound_17.play(when=win)  # sync with win flip
        if sound_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_17.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_17.tStop = t  # not accounting for scr refresh
                sound_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_17, 'tStopRefresh')  # time at next scr refresh
                sound_17.stop()
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 90-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simple_timingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simple_timing"-------
    for thisComponent in simple_timingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_8.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_8.started', sound_8.tStartRefresh)
    trials.addData('sound_8.stopped', sound_8.tStopRefresh)
    sound_9.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_9.started', sound_9.tStartRefresh)
    trials.addData('sound_9.stopped', sound_9.tStopRefresh)
    sound_10.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_10.started', sound_10.tStartRefresh)
    trials.addData('sound_10.stopped', sound_10.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_11.started', sound_11.tStartRefresh)
    trials.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_12.started', sound_12.tStartRefresh)
    trials.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_13.started', sound_13.tStartRefresh)
    trials.addData('sound_13.stopped', sound_13.tStopRefresh)
    sound_14.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_14.started', sound_14.tStartRefresh)
    trials.addData('sound_14.stopped', sound_14.tStopRefresh)
    sound_15.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_15.started', sound_15.tStartRefresh)
    trials.addData('sound_15.stopped', sound_15.tStopRefresh)
    sound_16.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_16.started', sound_16.tStartRefresh)
    trials.addData('sound_16.stopped', sound_16.tStopRefresh)
    sound_17.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_17.started', sound_17.tStartRefresh)
    trials.addData('sound_17.stopped', sound_17.tStopRefresh)
    trials.addData('text_9.started', text_9.tStartRefresh)
    trials.addData('text_9.stopped', text_9.tStopRefresh)
    outlet.push_sample(x=[1])
    
    # ------Prepare to start Routine "baseline"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('baseline.wav', hamming=True)
    sound_2.setVolume(1.0, log=False)
    outlet.push_sample(x=[3])
    # keep track of which components have finished
    baselineComponents = [text, sound_2]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    outlet.push_sample(x=[3])
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sync_simple_b"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_6.setSound('sync_simple_B.wav', hamming=True)
    sound_6.setVolume(1.0, log=False)
    # keep track of which components have finished
    sync_simple_bComponents = [text_6, sound_6]
    for thisComponent in sync_simple_bComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sync_simple_bClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sync_simple_b"-------
    while continueRoutine:
        # get current time
        t = sync_simple_bClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sync_simple_bClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sync_simple_bComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sync_simple_b"-------
    for thisComponent in sync_simple_bComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_6.started', text_6.tStartRefresh)
    trials.addData('text_6.stopped', text_6.tStopRefresh)
    sound_6.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_6.started', sound_6.tStartRefresh)
    trials.addData('sound_6.stopped', sound_6.tStopRefresh)
    # the Routine "sync_simple_b" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simple_timing"-------
    continueRoutine = True
    routineTimer.add(90.250000)
    # update component parameters for each repeat
    sound_8.setSound('A', secs=0.25, hamming=True)
    sound_8.setVolume(1.0, log=False)
    sound_9.setSound('A', secs=0.25, hamming=True)
    sound_9.setVolume(1.0, log=False)
    sound_10.setSound('A', secs=0.25, hamming=True)
    sound_10.setVolume(1.0, log=False)
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=0.25, hamming=True)
    sound_13.setVolume(1.0, log=False)
    sound_14.setSound('A', secs=0.25, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_15.setSound('A', secs=0.25, hamming=True)
    sound_15.setVolume(1.0, log=False)
    sound_16.setSound('A', secs=0.25, hamming=True)
    sound_16.setVolume(1.0, log=False)
    sound_17.setSound('A', secs=0.25, hamming=True)
    sound_17.setVolume(1.0, log=False)
    outlet.push_sample(x=[1])
    # keep track of which components have finished
    simple_timingComponents = [sound_8, sound_9, sound_10, sound_11, sound_12, sound_13, sound_14, sound_15, sound_16, sound_17, text_9]
    for thisComponent in simple_timingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    simple_timingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "simple_timing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = simple_timingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=simple_timingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play(when=win)  # sync with win flip
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play(when=win)  # sync with win flip
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        # start/stop sound_10
        if sound_10.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.tStart = t  # local t and not account for scr refresh
            sound_10.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10.play(when=win)  # sync with win flip
        if sound_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_10.tStop = t  # not accounting for scr refresh
                sound_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10, 'tStopRefresh')  # time at next scr refresh
                sound_10.stop()
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        # start/stop sound_14
        if sound_14.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14.play(when=win)  # sync with win flip
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14, 'tStopRefresh')  # time at next scr refresh
                sound_14.stop()
        # start/stop sound_15
        if sound_15.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
            # keep track of start time/frame for later
            sound_15.frameNStart = frameN  # exact frame index
            sound_15.tStart = t  # local t and not account for scr refresh
            sound_15.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15.play(when=win)  # sync with win flip
        if sound_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_15.tStop = t  # not accounting for scr refresh
                sound_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15, 'tStopRefresh')  # time at next scr refresh
                sound_15.stop()
        # start/stop sound_16
        if sound_16.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            sound_16.frameNStart = frameN  # exact frame index
            sound_16.tStart = t  # local t and not account for scr refresh
            sound_16.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16.play(when=win)  # sync with win flip
        if sound_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_16.tStop = t  # not accounting for scr refresh
                sound_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16, 'tStopRefresh')  # time at next scr refresh
                sound_16.stop()
        # start/stop sound_17
        if sound_17.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            sound_17.frameNStart = frameN  # exact frame index
            sound_17.tStart = t  # local t and not account for scr refresh
            sound_17.tStartRefresh = tThisFlipGlobal  # on global time
            sound_17.play(when=win)  # sync with win flip
        if sound_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_17.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_17.tStop = t  # not accounting for scr refresh
                sound_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_17, 'tStopRefresh')  # time at next scr refresh
                sound_17.stop()
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 90-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simple_timingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simple_timing"-------
    for thisComponent in simple_timingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_8.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_8.started', sound_8.tStartRefresh)
    trials.addData('sound_8.stopped', sound_8.tStopRefresh)
    sound_9.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_9.started', sound_9.tStartRefresh)
    trials.addData('sound_9.stopped', sound_9.tStopRefresh)
    sound_10.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_10.started', sound_10.tStartRefresh)
    trials.addData('sound_10.stopped', sound_10.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_11.started', sound_11.tStartRefresh)
    trials.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_12.started', sound_12.tStartRefresh)
    trials.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_13.started', sound_13.tStartRefresh)
    trials.addData('sound_13.stopped', sound_13.tStopRefresh)
    sound_14.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_14.started', sound_14.tStartRefresh)
    trials.addData('sound_14.stopped', sound_14.tStopRefresh)
    sound_15.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_15.started', sound_15.tStartRefresh)
    trials.addData('sound_15.stopped', sound_15.tStopRefresh)
    sound_16.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_16.started', sound_16.tStartRefresh)
    trials.addData('sound_16.stopped', sound_16.tStopRefresh)
    sound_17.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_17.started', sound_17.tStartRefresh)
    trials.addData('sound_17.stopped', sound_17.tStopRefresh)
    trials.addData('text_9.started', text_9.tStartRefresh)
    trials.addData('text_9.stopped', text_9.tStopRefresh)
    outlet.push_sample(x=[1])
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "finish"-------
continueRoutine = True
# update component parameters for each repeat
sound_1.setSound('Thats-All-Folks.wav', hamming=True)
sound_1.setVolume(1.0, log=False)
# keep track of which components have finished
finishComponents = [sound_1, text_8]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finish"-------
while continueRoutine:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
