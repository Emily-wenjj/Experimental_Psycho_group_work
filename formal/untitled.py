#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.5),
    on 十一月 18, 2026, at 17:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.5'
expName = 'untitled'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '',
    'gender': '',
    'age': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2048, 1152]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\大学\\实心\\小组实验\\raw material(1)\\untitled.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('debug')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='InnerTTY70', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "initialization" ---
    # Run 'Begin Experiment' code from general_setting
    from scipy.stats import wasserstein_distance
    
    from scipy.stats import binom, norm
    import numpy as np
    import pandas as pd
    import itertools
    import math
    
    os.chdir(_thisDir)
    
    win.mouseVisible = False
    current_mon = win.monitor
    x = np.concatenate((np.array([-5]),np.linspace(-1,+1,1001), np.array([5])))
    #selection_bar_width = 30
    #selection_bar_height = 4.5
    
    mean_bar_width = 0.004
    mean_bar_height = 0.03
    volcano_height = 0.05
    
    my_repeat = 3
    num_blocks= 6
    overall_cond = pd.read_csv('cond_file.csv')
    print(overall_cond.shape[0]*my_repeat)
    rest_trials = list(np.linspace(0, overall_cond.shape[0]*my_repeat, num_blocks+1))
    rest_trials = rest_trials[1:-1]
    print(rest_trials)
    
    exp_general = {'n_dots_per_fresh': 1,
                   'n_frame_per_fresh': 10,
                   'n_frame_per_empty': 10,
    #               'sample_bar_width': 0.003,
    #               'sample_bar_length': 0.1,
                   'sample_circ_width': 0.02,
                   'sample_alpha': 1,
                   'norm_fixation_color': [255,255,255],
                   'comparison_total': 150,
                   'comparison_alpha': 0.3,
                   'comparsion_distance': 3,
                   'jitter': 0.6,
                   'response_limit': 5,
                   'scale': 5
                   }
    
    if np.random.random() > 0.5:
        thisExp.addData('conf', 'low_con_left')
        instruction_img = 'low_con_left_ins.png'
        conf_text = 'a=没信心 , d＝有信心'
        low_conf_left = True
    else:
        thisExp.addData('conf', 'low_con_right')
        instruction_img = 'low_con_right_ins.png'
        conf_text = 'a=有信心 , d＝没信心'
        low_conf_left = False
    
    
    wms_dic= {0: {1: {'m': [0.0], 's': [0.19887041996880728], 'w': [1]},
         2: {'m': [0.28378378378378377, -0.0945945945945946],
             's': [0.02702702702702703, 0.13011721575751145],
             'w': [0.25, 0.75]},
         3: {'m': [0.06756756756756757, 0.28378378378378377, -0.17567567567567569],
             's': [0.02702702702702703, 0.02702702702702703, 0.07279215563327314],
             'w': [0.25, 0.25, 0.5]},
         4: {'m': [-0.24324324324324326,
                   -0.10810810810810811,
                   0.06756756756756757,
                   0.28378378378378377],
             's': [0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703],
             'w': [0.25, 0.25, 0.25, 0.25]}},
     1: {1: {'m': [0.0], 's': [0.20357400895852606], 'w': [1]},
         2: {'m': [-0.1858108108108108, 0.1858108108108108],
             's': [0.07281841796196412, 0.09190303569056915],
             'w': [0.5, 0.5]},
         3: {'m': [0.09797297297297297, 0.27364864864864863, -0.1858108108108108],
             's': [0.02702702702702703, 0.02702702702702703, 0.07280569111078869],
             'w': [0.25, 0.25, 0.5]},
         4: {'m': [-0.2533783783783784,
                   -0.11824324324324324,
                   0.09797297297297297,
                   0.27364864864864863],
             's': [0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703],
             'w': [0.25, 0.25, 0.25, 0.25]}},
     2: {1: {'m': [0.0], 's': [0.19417320835791227], 'w': [1]},
         2: {'m': [0.27364864864864863, -0.09121621621621621],
             's': [0.02702702702702703, 0.13011562715899094],
             'w': [0.25, 0.75]},
         3: {'m': [-0.2533783783783784, 0.27364864864864863, -0.010135135135135136],
             's': [0.02702702702702703, 0.02702702702702703, 0.07276652341636755],
             'w': [0.25, 0.25, 0.5]},
         4: {'m': [-0.2533783783783784,
                   -0.0777027027027027,
                   0.057432432432432436,
                   0.27364864864864863],
             's': [0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703],
             'w': [0.25, 0.25, 0.25, 0.25]}},
     3: {1: {'m': [0.0], 's': [0.20358812495401726], 'w': [1]},
         2: {'m': [-0.1858108108108108, 0.1858108108108108],
             's': [0.09190656699148862, 0.07277259310637003],
             'w': [0.5, 0.5]},
         3: {'m': [-0.27364864864864863, -0.09797297297297297, 0.1858108108108108],
             's': [0.02702702702702703, 0.02702702702702703, 0.07278745632137709],
             'w': [0.25, 0.25, 0.5]},
         4: {'m': [-0.27364864864864863,
                   -0.09797297297297297,
                   0.11824324324324324,
                   0.2533783783783784],
             's': [0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703],
             'w': [0.25, 0.25, 0.25, 0.25]}},
     4: {1: {'m': [0.0], 's': [0.19446182350824087], 'w': [1]},
         2: {'m': [-0.27364864864864863, 0.09121621621621621],
             's': [0.02702702702702703, 0.13006314423279944],
             'w': [0.25, 0.75]},
         3: {'m': [-0.27364864864864863, 0.2533783783783784, 0.010135135135135136],
             's': [0.02702702702702703, 0.02702702702702703, 0.07278682171136365],
             'w': [0.25, 0.25, 0.5]},
         4: {'m': [-0.27364864864864863,
                   -0.057432432432432436,
                   0.0777027027027027,
                   0.2533783783783784],
             's': [0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703],
             'w': [0.25, 0.25, 0.25, 0.25]}},
     5: {1: {'m': [0.0], 's': [0.19914499030848157], 'w': [1]},
         2: {'m': [-0.28378378378378377, 0.0945945945945946],
             's': [0.02702702702702703, 0.13007948917521175],
             'w': [0.25, 0.75]},
         3: {'m': [-0.28378378378378377, -0.06756756756756757, 0.17567567567567569],
             's': [0.02702702702702703, 0.02702702702702703, 0.07278438519372651],
             'w': [0.25, 0.25, 0.5]},
         4: {'m': [-0.28378378378378377,
                   -0.06756756756756757,
                   0.10810810810810811,
                   0.24324324324324326],
             's': [0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703,
                   0.02702702702702703],
             'w': [0.25, 0.25, 0.25, 0.25]}}}
    
    def gen_mixture_pdf(weight_list, mean_list, sigma_list):
        assert len(weight_list) == len(mean_list) and len(mean_list) == len(
            sigma_list), 'Please provide equal length weight_list, mean_list, sigma_list'
        assert np.abs(np.sum(weight_list)-1) < 0.01, 'The weight should sum to one'
    
        def mixture_pdf(x):
            def gen_single_pdf(weight, mean, sigma):
                def pdf(my_x):
                    return weight * norm.pdf(my_x, mean, sigma)
    
                return pdf
    
            pdf_list = []
            for my_weight, my_mean, my_sigma in zip(weight_list, mean_list, sigma_list):
                pdf_list.append(gen_single_pdf(my_weight, my_mean, my_sigma))
    
            each_density = np.array([my_pdf(x) for my_pdf in pdf_list])
    
            return np.sum(each_density, axis=0)
    
        return mixture_pdf
    
    def bounded_mixture_rvs(weight_list, mean_list, sigma_list, sample_size, my_range):
        assert len(weight_list) == len(mean_list) and len(mean_list) == len(
            sigma_list), 'Please provide equal length weight_list, mean_list, sigma_list'
        assert np.abs(np.sum(weight_list)-1) < 0.001, 'The weight should sum to one'
    
        num_in_each = np.random.multinomial(sample_size, weight_list)
        samples = []
        for mixture_idx, mixture_num in enumerate(num_in_each):
            stuff = norm.rvs(mean_list[mixture_idx], sigma_list[mixture_idx], mixture_num)
            samples.append(stuff)
    
        all_samples = np.concatenate(samples)
        all_samples = all_samples[np.logical_and(all_samples > my_range[0], all_samples < my_range[1])]
    
        num_resample = sample_size - all_samples.shape[0]
    #     print(num_resample)
    
        if num_resample  > 0:
            resamples =  bounded_mixture_rvs(weight_list, mean_list, sigma_list, num_resample, my_range)
        else:
            resamples = np.array([])
        return np.random.permutation(np.concatenate((all_samples, resamples)))
    
    def mixture_rvs(weight_list, mean_list, sigma_list, sample_size):
        assert len(weight_list) == len(mean_list) and len(mean_list) == len(
            sigma_list), 'Please provide equal length weight_list, mean_list, sigma_list'
        assert np.abs(np.sum(weight_list)-1) < 0.01, 'The weight should sum to one'
    
        num_in_each = np.random.multinomial(sample_size, weight_list)
    
        samples = []
        for mixture_idx, mixture_num in enumerate(num_in_each):
            stuff = norm.rvs(mean_list[mixture_idx], sigma_list[mixture_idx], mixture_num)
            samples.append(stuff)
    
        return np.random.permutation(np.concatenate(samples))
    
    y_of_the_axis_line = -0.2
    reference_line = visual.Line(
        win=win, name='reference_line',units='height', 
        start=(-(2, 0.5)[0]/2.0, 0), end=(+(2, 0.5)[0]/2.0, 0),
        ori=0, pos=[0,y_of_the_axis_line],
        lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    
    
    #sti_folder = 'my_sti/' + expInfo['participant'] + '/'
    #if not os.path.exists(sti_folder):
    #    os.mkdir(sti_folder)
    #    os.mkdir(sti_folder + 'stimulus/')
    #    os.mkdir(sti_folder + 'comp_sti/')
    
    # --- Initialize components for Routine "inst" ---
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.98*1.7, 0.98),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "see_what_will_happen" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='那么年轻的魔法学徒，我们来进行一下练习试次吧！\n（按空格继续）',
        font='Microsoft YaHei',
        units='height', pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', units='height', 
        image='123.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "empty" ---
    hello = visual.TextStim(win=win, name='hello',
        text=' ',
        font='Microsoft YaHei',
        units='pix', pos=(0, 0), draggable=False, height=200, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "before_pac1" ---
    
    # --- Initialize components for Routine "prac_1_magic" ---
    
    # --- Initialize components for Routine "fixation" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "sti_present" ---
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "fixation" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "reproduction" ---
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code
    
    
    
    
    # --- Initialize components for Routine "normalization" ---
    text = visual.TextStim(win=win, name='text',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "empty" ---
    hello = visual.TextStim(win=win, name='hello',
        text=' ',
        font='Microsoft YaHei',
        units='pix', pos=(0, 0), draggable=False, height=200, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "end_prac" ---
    
    # --- Initialize components for Routine "before_main" ---
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', units='height', 
        image='123.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_7 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    text_7 = visual.TextStim(win=win, name='text_7',
        text='那么年轻的魔法学徒，我们开始正式实验吧！\n（按空格继续）',
        font='Microsoft YaHei',
        units='height', pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "main_magic" ---
    
    # --- Initialize components for Routine "fixation" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "sti_present" ---
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "fixation" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "reproduction" ---
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code
    
    
    
    
    # --- Initialize components for Routine "normalization" ---
    text = visual.TextStim(win=win, name='text',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "empty" ---
    hello = visual.TextStim(win=win, name='hello',
        text=' ',
        font='Microsoft YaHei',
        units='pix', pos=(0, 0), draggable=False, height=200, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "inter_block_rest" ---
    # Run 'Begin Experiment' code from code_7
    rest_text  = ' '
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Microsoft YaHei',
        units='pix', pos=(0, 0), draggable=False, height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "space_to_start" ---
    key_resp_5 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='当你准备好之后，\n按空格继续实验',
        font='Microsoft YaHei',
        units='pix', pos=(0, 0), draggable=False, height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "end" ---
    # Run 'Begin Experiment' code from code_9
    last_msg = ' '
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Microsoft YaHei',
        units='pix', pos=(0, 0), draggable=False, height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_6 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "initialization" ---
    # create an object to store info about Routine initialization
    initialization = data.Routine(
        name='initialization',
        components=[],
    )
    initialization.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for initialization
    initialization.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    initialization.tStart = globalClock.getTime(format='float')
    initialization.status = STARTED
    thisExp.addData('initialization.started', initialization.tStart)
    initialization.maxDuration = None
    # keep track of which components have finished
    initializationComponents = initialization.components
    for thisComponent in initialization.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "initialization" ---
    thisExp.currentRoutine = initialization
    initialization.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=initialization,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            initialization.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if initialization.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in initialization.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "initialization" ---
    for thisComponent in initialization.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for initialization
    initialization.tStop = globalClock.getTime(format='float')
    initialization.tStopRefresh = tThisFlipGlobal
    thisExp.addData('initialization.stopped', initialization.tStop)
    thisExp.nextEntry()
    # the Routine "initialization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "inst" ---
    # create an object to store info about Routine inst
    inst = data.Routine(
        name='inst',
        components=[image_2],
    )
    inst.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    image_list = ['inst', 'quest', 'dist_basic', 'dist_adva', 'dist_over_all', 'dist_different', 'procedure']
    image_list = [i + '.png' for i in image_list]
    current_index = 0
    current_image = image_list[current_index]
    
    key_resp_2 = keyboard.Keyboard()
    # store start times for inst
    inst.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    inst.tStart = globalClock.getTime(format='float')
    inst.status = STARTED
    thisExp.addData('inst.started', inst.tStart)
    inst.maxDuration = None
    # keep track of which components have finished
    instComponents = inst.components
    for thisComponent in inst.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "inst" ---
    thisExp.currentRoutine = inst
    inst.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_6
        keys = key_resp_2.getKeys(keyList=['left', 'right', 'p'])
        #print(keys)
        if len(keys) > 0:
            pressed_key = keys[0]
            if pressed_key == 'right':
                current_index += 1
            elif pressed_key == 'left':
                current_index -= 1
            elif pressed_key == 'p':
                continueRoutine = False
                
            current_index = np.max([0, current_index %len(image_list)])
            current_image = image_list[current_index]
            
        
        
        
        
        # *image_2* updates
        
        # if image_2 is starting this frame...
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            # update status
            image_2.status = STARTED
            image_2.setAutoDraw(True)
        
        # if image_2 is active this frame...
        if image_2.status == STARTED:
            # update params
            image_2.setImage(current_image, log=False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=inst,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            inst.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if inst.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in inst.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inst" ---
    for thisComponent in inst.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for inst
    inst.tStop = globalClock.getTime(format='float')
    inst.tStopRefresh = tThisFlipGlobal
    thisExp.addData('inst.stopped', inst.tStop)
    thisExp.nextEntry()
    # the Routine "inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "see_what_will_happen" ---
    # create an object to store info about Routine see_what_will_happen
    see_what_will_happen = data.Routine(
        name='see_what_will_happen',
        components=[text_3, key_resp_3, image_3],
    )
    see_what_will_happen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for see_what_will_happen
    see_what_will_happen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    see_what_will_happen.tStart = globalClock.getTime(format='float')
    see_what_will_happen.status = STARTED
    thisExp.addData('see_what_will_happen.started', see_what_will_happen.tStart)
    see_what_will_happen.maxDuration = None
    # keep track of which components have finished
    see_what_will_happenComponents = see_what_will_happen.components
    for thisComponent in see_what_will_happen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "see_what_will_happen" ---
    thisExp.currentRoutine = see_what_will_happen
    see_what_will_happen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *image_3* updates
        
        # if image_3 is starting this frame...
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            # update status
            image_3.status = STARTED
            image_3.setAutoDraw(True)
        
        # if image_3 is active this frame...
        if image_3.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=see_what_will_happen,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            see_what_will_happen.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if see_what_will_happen.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in see_what_will_happen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "see_what_will_happen" ---
    for thisComponent in see_what_will_happen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for see_what_will_happen
    see_what_will_happen.tStop = globalClock.getTime(format='float')
    see_what_will_happen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('see_what_will_happen.stopped', see_what_will_happen.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "see_what_will_happen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "empty" ---
    # create an object to store info about Routine empty
    empty = data.Routine(
        name='empty',
        components=[hello],
    )
    empty.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for empty
    empty.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    empty.tStart = globalClock.getTime(format='float')
    empty.status = STARTED
    thisExp.addData('empty.started', empty.tStart)
    empty.maxDuration = None
    # keep track of which components have finished
    emptyComponents = empty.components
    for thisComponent in empty.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "empty" ---
    thisExp.currentRoutine = empty
    empty.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hello* updates
        
        # if hello is starting this frame...
        if hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hello.frameNStart = frameN  # exact frame index
            hello.tStart = t  # local t and not account for scr refresh
            hello.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hello, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'hello.started')
            # update status
            hello.status = STARTED
            hello.setAutoDraw(True)
        
        # if hello is active this frame...
        if hello.status == STARTED:
            # update params
            pass
        
        # if hello is stopping this frame...
        if hello.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hello.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                hello.tStop = t  # not accounting for scr refresh
                hello.tStopRefresh = tThisFlipGlobal  # on global time
                hello.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hello.stopped')
                # update status
                hello.status = FINISHED
                hello.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=empty,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            empty.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if empty.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in empty.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "empty" ---
    for thisComponent in empty.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for empty
    empty.tStop = globalClock.getTime(format='float')
    empty.tStopRefresh = tThisFlipGlobal
    thisExp.addData('empty.stopped', empty.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if empty.maxDurationReached:
        routineTimer.addTime(-empty.maxDuration)
    elif empty.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "before_pac1" ---
    # create an object to store info about Routine before_pac1
    before_pac1 = data.Routine(
        name='before_pac1',
        components=[],
    )
    before_pac1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_11
    total_w = 0
    # store start times for before_pac1
    before_pac1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    before_pac1.tStart = globalClock.getTime(format='float')
    before_pac1.status = STARTED
    thisExp.addData('before_pac1.started', before_pac1.tStart)
    before_pac1.maxDuration = None
    # keep track of which components have finished
    before_pac1Components = before_pac1.components
    for thisComponent in before_pac1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "before_pac1" ---
    thisExp.currentRoutine = before_pac1
    before_pac1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=before_pac1,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            before_pac1.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if before_pac1.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in before_pac1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "before_pac1" ---
    for thisComponent in before_pac1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for before_pac1
    before_pac1.tStop = globalClock.getTime(format='float')
    before_pac1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('before_pac1.stopped', before_pac1.tStop)
    thisExp.nextEntry()
    # the Routine "before_pac1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac1 = data.TrialHandler2(
        name='prac1',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('cond_file.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(prac1)  # add the loop to the experiment
    thisPrac1 = prac1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac1.rgb)
    if thisPrac1 != None:
        for paramName in thisPrac1:
            globals()[paramName] = thisPrac1[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPrac1 in prac1:
        prac1.status = STARTED
        if hasattr(thisPrac1, 'status'):
            thisPrac1.status = STARTED
        currentLoop = prac1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPrac1.rgb)
        if thisPrac1 != None:
            for paramName in thisPrac1:
                globals()[paramName] = thisPrac1[paramName]
        
        # --- Prepare to start Routine "prac_1_magic" ---
        # create an object to store info about Routine prac_1_magic
        prac_1_magic = data.Routine(
            name='prac_1_magic',
            components=[],
        )
        prac_1_magic.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_12
        current_session = prac1
        #prac1.finished = True
        #
        # store start times for prac_1_magic
        prac_1_magic.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prac_1_magic.tStart = globalClock.getTime(format='float')
        prac_1_magic.status = STARTED
        thisExp.addData('prac_1_magic.started', prac_1_magic.tStart)
        prac_1_magic.maxDuration = None
        # keep track of which components have finished
        prac_1_magicComponents = prac_1_magic.components
        for thisComponent in prac_1_magic.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_1_magic" ---
        thisExp.currentRoutine = prac_1_magic
        prac_1_magic.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=prac_1_magic,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                prac_1_magic.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if prac_1_magic.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in prac_1_magic.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_1_magic" ---
        for thisComponent in prac_1_magic.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prac_1_magic
        prac_1_magic.tStop = globalClock.getTime(format='float')
        prac_1_magic.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prac_1_magic.stopped', prac_1_magic.tStop)
        # the Routine "prac_1_magic" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_2],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            reference_line.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "sti_present" ---
        # create an object to store info about Routine sti_present
        sti_present = data.Routine(
            name='sti_present',
            components=[key_resp],
        )
        sti_present.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from present_bars
        #sti_base_type = 0
        #sti_cluster_number = 1
        #sample_size = 20
        #scale = 3 # if you are going to jitter the mean, take care!
        mouse.setVisible(0)
        small_bars = visual.ElementArrayStim(
                win=win,
                nElements=exp_general['n_dots_per_fresh'],
                elementTex=np.ones([16, 16]),
                elementMask="circle",
                sfs=0,
                xys=np.zeros((exp_general['n_dots_per_fresh'],2)),
                sizes=[exp_general['sample_circ_width'], exp_general['sample_circ_width']],
                oris=0, units='height', opacities=exp_general['sample_alpha'],colors = [1,-1,-1])
        
        my_overall_mean_jitter = (np.random.random()-0.5)*2*0.2
        
        weights_of_sampler = np.array(wms_dic[sti_base_type][sti_cluster_number]['w'])
        means_of_sampler = np.array(wms_dic[sti_base_type][sti_cluster_number]['m'])  + my_overall_mean_jitter
        sds_of_sampler = np.array(wms_dic[sti_base_type][sti_cluster_number]['s']) 
        
        my_stimulus = bounded_mixture_rvs(weights_of_sampler, 
                                  means_of_sampler,
                                  sds_of_sampler, sample_size, (my_overall_mean_jitter- 3 * 0.2, my_overall_mean_jitter+ 3 * 0.2))
        
        my_stimulus = my_stimulus.reshape((-1,exp_general['n_dots_per_fresh']))
        current_session.addData('sti', my_stimulus)
        current_session.addData('my_true_luster_mean', means_of_sampler)
        
        
        #画一下真实分布PDF做测试参考
        mix_pdf = gen_mixture_pdf(weights_of_sampler,means_of_sampler,sds_of_sampler)
        x_axis = np.linspace(-0.5,0.5,50)
        pdf_points = [(x,mix_pdf(x)*0.2-0.2) for x in x_axis]
        debug_curve = visual.ShapeStim(win,vertices = pdf_points,lineColor = "blue",closeShape = False)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for sti_present
        sti_present.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        sti_present.tStart = globalClock.getTime(format='float')
        sti_present.status = STARTED
        thisExp.addData('sti_present.started', sti_present.tStart)
        sti_present.maxDuration = None
        # keep track of which components have finished
        sti_presentComponents = sti_present.components
        for thisComponent in sti_present.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "sti_present" ---
        thisExp.currentRoutine = sti_present
        sti_present.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from present_bars
            reference_line.draw()
            #计算刺激呈现周期
            index_with_in_big_refresh = frameN % (exp_general['n_frame_per_fresh'] + exp_general['n_frame_per_empty'])
            if math.floor(index_with_in_big_refresh/exp_general['n_frame_per_fresh']) == 0:
            #应该亮起的帧数
            #每个火山石10帧（167ms）
                if index_with_in_big_refresh % exp_general['n_frame_per_fresh'] == 0: # Set the new samples to their location
                    row_index = math.floor(frameN/(exp_general['n_frame_per_fresh'] + exp_general['n_frame_per_empty']))
                    current_sti = my_stimulus[row_index, :]
                    new_position = np.array([current_sti, np.ones(exp_general['n_dots_per_fresh']) * y_of_the_axis_line+exp_general['sample_circ_width']/2, ]).T
                    small_bars.xys = new_position
                small_bars.draw()
            else: 
            #空白帧数
                if row_index == my_stimulus.shape[0]-1:
                    continueRoutine = False
                    
            
            #debug curve
            debug_curve.draw()
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=sti_present,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                sti_present.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if sti_present.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in sti_present.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "sti_present" ---
        for thisComponent in sti_present.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for sti_present
        sti_present.tStop = globalClock.getTime(format='float')
        sti_present.tStopRefresh = tThisFlipGlobal
        thisExp.addData('sti_present.stopped', sti_present.tStop)
        # the Routine "sti_present" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_2],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            reference_line.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "reproduction" ---
        # create an object to store info about Routine reproduction
        reproduction = data.Routine(
            name='reproduction',
            components=[mouse],
        )
        reproduction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code
        current_state = 'determine_cluster_mean'
        mouse.setVisible(1)
        mouse.setPos((np.random.random()-0.5, y_of_the_axis_line))
        pos = mouse.getPos()
        key_resp = keyboard.Keyboard()
        mean_choice_rts = []
        mean_choices = []
        
        cluster_choice_order_list = []
        cluster_choice_rt_list = []
        
        height_sd_order_list = []
        height_sd_time_list = []
        
        #画分布线，在横轴上取很多点
        x = np.concatenate((np.array([-5]),np.linspace(-1,+1,1001), np.array([5])))
        
        #一阶段瞄准线
        my_mean_estimation_bar = visual.rect.Rect(win = win, width = mean_bar_width, height = mean_bar_height, lineColor  = 'white',lineWidth =2,
                          units = 'height', fillColor = 'white', pos = (pos[0], y_of_the_axis_line))
        
        height_bar_width = 0.005
        height_bar_height = 0
        
        #综合概率包络线
        overall_line = visual.ShapeStim(
                win=win,
                lineColor='#0066CC',
                closeShape=False, units = 'height', lineWidth = 6, fillColor = 'white',
                opacity = 0.5,vertices = [[0,0]])
        
        #
        mean_bar_list = []
        
        pdf_line_list = []
        height_bar_list = []
        width_bar_list = []
        
        width_bar_left_cap_list = []
        width_bar_right_cap_list = []
        
        left_button_have_been_clicked = False
        
        #指导语
        rep_instruction = visual.TextStim(win,text = "单击鼠标左键选择火山位置，按f提交\n单击火山调整火山的范围及权重\n按Enter提交",
        pos = (-0.72,0.38),height = 0.05,color = "white",font = "SimHei",alignHoriz = "left",wrapWidth = 0.3)
        # store start times for reproduction
        reproduction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reproduction.tStart = globalClock.getTime(format='float')
        reproduction.status = STARTED
        thisExp.addData('reproduction.started', reproduction.tStart)
        reproduction.maxDuration = None
        # keep track of which components have finished
        reproductionComponents = reproduction.components
        for thisComponent in reproduction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reproduction" ---
        thisExp.currentRoutine = reproduction
        reproduction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse.prevButtonState = mouse.getPressed()
            # Run 'Each Frame' code from code
            keys = key_resp.getKeys(keyList=['f', 'return'])
            pos = mouse.getPos()
            clicked_buttons, click_time = mouse.getPressed(getTime = True)
            left_button_clicked = clicked_buttons[0]
            #一阶段：找到火山
            if current_state == 'determine_cluster_mean': # In this stage, participants need to use mouse to mark the location of different cluster centers
                my_mean_estimation_bar.pos = (pos[0], y_of_the_axis_line)
                if left_button_clicked:
                    left_button_have_been_clicked = True
                #检测鼠标松开的瞬间
                elif (left_button_clicked == 0) and left_button_have_been_clicked:
                    #防止火山重叠
                    if np.all(np.abs(np.array(mean_choices) - pos[0]) > mean_bar_height/2):
                        left_button_have_been_clicked = False
                        #记录点击位置和时间
                        mean_choice_rts.append(t)
                        mean_choices.append(pos[0])
                        my_mean_bar = visual.ImageStim(
                    win=win,
                    image='volcano.png', mask=None,
                    ori=0.0, pos=(pos[0], y_of_the_axis_line+mean_bar_height/2), size=(mean_bar_height, mean_bar_height),
                    color=[1,1,1], colorSpace='rgb', opacity=0.4,
                    flipHoriz=False, flipVert=False,units = 'height',
                    texRes=128.0, interpolate=True, depth=-1.0)
                        mean_bar_list.append(my_mean_bar)
                    else:
                        left_button_have_been_clicked = False
            
                elif len(keys) > 0 and len(mean_choices)>=1:
                    pressed_key = keys[0]
                        
                    if pressed_key == 'f':
                        #结束找火山，等待被试选择估计哪个火山的范围和权重
                        left_button_have_been_clicked = False
                        current_state = 'determin_which_cluster_to_assign_weight_and_SD'
                        num_clusters = len(mean_bar_list)
            
                        height_list = [0] * num_clusters
                        sd_list = [0.005] * num_clusters
                        mean_list = [i.pos[0] for i in mean_bar_list]
                        
                        #建立一些有待后续使用的神秘对象
                        pdf_line_list = [visual.ShapeStim(win=win,lineColor='white',closeShape=False, 
                                         units = 'height', lineWidth = 3, fillColor = 'white',opacity = 0.5,vertices = [[0,0]])
                                         for i in range(num_clusters)]
                        height_bar_list = [visual.rect.Rect(win = win, width = height_bar_width, height = 0, lineColor = '#0066CC',lineWidth =2,
                                           units = 'height', fillColor = '#0066CC', pos = (m,y_of_the_axis_line)) for m in mean_list]
            
                        width_bar_list = [visual.rect.Rect(win = win, width = 0, height = 0.002, lineColor  = '#FF9900',lineWidth =0,
                                           units = 'height', fillColor = '#FF9900', pos = (m,y_of_the_axis_line), opacity = 0.5) for m in mean_list]
                                           
                        width_bar_left_cap_list = [visual.rect.Rect(win = win, width = 0.002, height = 0.03, lineColor  = '#FF9900',lineWidth =0,
                                           units = 'height', fillColor = '#FF9900', pos = (m,y_of_the_axis_line), opacity = 0.5) for m in mean_list]
                        width_bar_right_cap_list = [visual.rect.Rect(win = win, width = 0.002, height = 0.03, lineColor  = '#FF9900',lineWidth =0,
                                           units = 'height', fillColor = '#FF9900', pos = (m,y_of_the_axis_line), opacity = 0.5) for m in mean_list]
            
                        mouse.setVisible(1)
                        #隐藏瞄准线
                        my_mean_estimation_bar.opacity = 0
            
            elif current_state == 'determin_which_cluster_to_assign_weight_and_SD': # In this stage, participants need to click the white mean bar and enter the 'adjuct_weight_and_SD' stage
                for bar_index, current_bar in enumerate(mean_bar_list):
                    #如果被试点击了某一个火山
                    if mouse.isPressedIn(current_bar):
                        left_button_have_been_clicked = True
                        selected_index = bar_index
                    elif (left_button_clicked == 0) and left_button_have_been_clicked and selected_index == bar_index:
                        left_button_have_been_clicked = False
                        
                        #取出刚刚表格中对应对象
                        my_line = pdf_line_list[bar_index]
                        current_height_bar = height_bar_list[bar_index]
                        current_width_bar = width_bar_list[bar_index]
                        current_state = 'adjuct_weight_and_SD'
                        mean_of_the_cluster = mean_choices[bar_index]
                        width_bar_left_cap = width_bar_left_cap_list[bar_index]
                        width_bar_right_cap = width_bar_right_cap_list[bar_index]
                        
                        #让选中的火山亮起
                        current_bar.opacity = 1
                        selected_index = bar_index
                        
                        cluster_choice_order_list.append(selected_index)
                        cluster_choice_rt_list.append(t)
                        
                #调完之后提交
                if len(keys) > 0: 
                    pressed_key = keys[0]
                    if pressed_key == 'return' and np.all([i.opacity == 1 for i in mean_bar_list]):
                        continueRoutine = False
                        current_session.addData('mean_list', mean_list)#每个火山的位置
                        current_session.addData('height_list', height_list)#每个火山分布的中心高度
                        current_session.addData('sd_list', sd_list)#每个火山分布的标准差
                        current_session.addData('mean_click_rt', mean_choice_rts)
                        current_session.addData('cluster_choice_order_list', cluster_choice_order_list)
                        current_session.addData('cluster_choice_rt_list', cluster_choice_rt_list)
                        current_session.addData('height_sd_order_list', height_sd_order_list)
                        current_session.addData('height_sd_time_list', height_sd_time_list)
                        
            
            elif current_state == 'adjuct_weight_and_SD': # In this stage, participants need to adjust the weight and SD of the selected cluster
                my_width = np.max([0.005,np.abs(pos[0]-mean_of_the_cluster)]) # take care! it's 65% area!!
                my_std = my_width/0.934
                my_height = np.max([0, pos[1]-y_of_the_axis_line])
                dist_height_scale_factor = norm.pdf(0, loc = 0, scale = my_std)
                
                
                
                sd_list[selected_index] = my_std
                height_list[selected_index] = my_height
                
                #更改大包络线的设置
                all_heights = np.array([norm.pdf(x, loc = mean_list[i], scale = sd_list[i])* height_list[i]/norm.pdf(0, loc = 0, scale = sd_list[i]) for i in range(num_clusters)])
                sumed_heights = np.sum(all_heights, axis = 0)
                normalizing_factor = 1
                sumed_heights = sumed_heights / normalizing_factor
                overall_y = sumed_heights + y_of_the_axis_line
                overall_line.vertices = np.array((x, overall_y)).T
                
                #画当前火山的分布线
                current_height_bar.height = my_height
                current_height_bar.pos = [mean_of_the_cluster, y_of_the_axis_line + my_height/2]
                current_width_bar.width = my_width*2
                
                width_bar_left_cap.pos = [mean_of_the_cluster-my_width, y_of_the_axis_line]
                width_bar_right_cap.pos = [mean_of_the_cluster+my_width, y_of_the_axis_line]
                
                
                y = norm.pdf(x, loc = mean_of_the_cluster, scale = my_std) * my_height/dist_height_scale_factor+y_of_the_axis_line
                my_line.vertices = np.array((x,y)).T
                my_line.closeShape = True
                my_line.draw()
                
                #let's try it
                #current_width_bar.draw()
                #width_bar_left_cap.draw()
                #current_height_bar.draw()
                
                #完成一个火山之后返回等待状态
                if left_button_clicked:
                    left_button_have_been_clicked = True
                elif (left_button_clicked == 0) and left_button_have_been_clicked:
                    height_list[selected_index] = my_height
                    sd_list[selected_index] = my_std
                    
                    height_sd_order_list.append([my_height, my_std])
                    height_sd_time_list.append(t)
                    
                    left_button_have_been_clicked = False
                    current_state = 'determin_which_cluster_to_assign_weight_and_SD'
            
            
            #轴线
            reference_line.draw()
            
            
            #画出所有火山
            for i in mean_bar_list:
                i.draw()
                
            #画总分布线
            overall_line.draw()
            
            #瞄准线
            my_mean_estimation_bar.draw()
            
            #显示指导语
            rep_instruction.draw()
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=reproduction,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                reproduction.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if reproduction.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in reproduction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reproduction" ---
        for thisComponent in reproduction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reproduction
        reproduction.tStop = globalClock.getTime(format='float')
        reproduction.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reproduction.stopped', reproduction.tStop)
        # store data for prac1 (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        prac1.addData('mouse.x', x)
        prac1.addData('mouse.y', y)
        prac1.addData('mouse.leftButton', buttons[0])
        prac1.addData('mouse.midButton', buttons[1])
        prac1.addData('mouse.rightButton', buttons[2])
        # the Routine "reproduction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "normalization" ---
        # create an object to store info about Routine normalization
        normalization = data.Routine(
            name='normalization',
            components=[text],
        )
        normalization.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        overall_line = visual.ShapeStim(
                win=win,
                lineColor='#0066CC',
                closeShape=False, units = 'height', lineWidth = 6, fillColor = 'white',
                opacity = 0.5,vertices = [[0,0]])
        x = np.concatenate((np.array([-5]),np.linspace(-1,+1,1001), np.array([5])))
        #对每个火山，计算每个点的高度，所有火山加和形成总包络线
        #all_heights:每一行是一座火山，K行*1001列
        all_heights = np.array([my_pdf_line.vertices[:,1]-y_of_the_axis_line for my_pdf_line in pdf_line_list])
        sumed_heights = np.sum(all_heights, axis = 0)#把每一列加和，得到1*1001
        normalizing_factor = 1 # ?历史遗留问题
        sumed_heights = sumed_heights / normalizing_factor
        overall_y = sumed_heights + y_of_the_axis_line
        overall_line.vertices = np.array((x, overall_y)).T
        
        
        weight_list = np.sum(all_heights, axis = 1)/ np.sum(sumed_heights)#axis = 1:把每一行加和，得到单个火山下的面积
        current_session.addData('weight_list', weight_list)#得到权重分配
        
        #也是历史遗留问题
        for i in pdf_line_list:
            i.vertices = np.array((x, (i.vertices[:, -1] - y_of_the_axis_line) / normalizing_factor+ y_of_the_axis_line)).T
        
        #用真实分布和被试报告的分布分别取样，计算wasserstein距离，评价作答准确性
        u_dist = bounded_mixture_rvs(weights_of_sampler, 
                                  means_of_sampler,
                                  sds_of_sampler, 10000,(my_overall_mean_jitter- 2.8 * 0.2, my_overall_mean_jitter+ 2.8 * 0.2))
        
        v_dist = bounded_mixture_rvs(weight_list, 
                                  mean_list,
                                  sd_list, 10000,(my_overall_mean_jitter- 2.8 * 0.2, my_overall_mean_jitter+ 2.8 * 0.2))
        
        w_distance = wasserstein_distance(u_dist, v_dist)
        total_w += w_distance
        current_session.addData('w_distance', w_distance)
        
        
        my_stimulus = my_stimulus.reshape(-1)
        #展示真实曲线和真实刺激点？不需要
        feedback_line = visual.ShapeStim(
                win=win,
                lineColor='green',
                closeShape=False, units = 'height', lineWidth = 6, fillColor = 'white',
                opacity = 0.5,vertices = [[0,0]])
        my_pdf = gen_mixture_pdf(weights_of_sampler, 
                                  means_of_sampler,
                                  sds_of_sampler)
        feedback_height = np.sum(sumed_heights) * my_pdf(x)/np.sum(my_pdf(x))+y_of_the_axis_line
        feedback_line.vertices = np.array((x, feedback_height)).T
        
        my_stimulus = my_stimulus.reshape(-1)
        feedback_dots = visual.ElementArrayStim(
                win=win,
                nElements=sample_size,
                elementTex=np.ones([16, 16]),
                elementMask="circle",
                sfs=0,
                xys=np.array((my_stimulus, y_of_the_axis_line + (np.random.random(sample_size)-0.5)/100)).T,
                sizes=[exp_general['sample_circ_width'], exp_general['sample_circ_width']],
                oris=0, units='height', opacities=0.3,colors = [1,-1,-1])
        # store start times for normalization
        normalization.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        normalization.tStart = globalClock.getTime(format='float')
        normalization.status = STARTED
        thisExp.addData('normalization.started', normalization.tStart)
        normalization.maxDuration = None
        # keep track of which components have finished
        normalizationComponents = normalization.components
        for thisComponent in normalization.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "normalization" ---
        thisExp.currentRoutine = normalization
        normalization.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            #每个火山的分布线
            for i in pdf_line_list:
                i.draw()
            #总和分布线
            overall_line.draw()
            
            #画所有火山
            for i in mean_bar_list:
                i.draw()
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=normalization,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                normalization.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if normalization.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in normalization.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "normalization" ---
        for thisComponent in normalization.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for normalization
        normalization.tStop = globalClock.getTime(format='float')
        normalization.tStopRefresh = tThisFlipGlobal
        thisExp.addData('normalization.stopped', normalization.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if normalization.maxDurationReached:
            routineTimer.addTime(-normalization.maxDuration)
        elif normalization.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "empty" ---
        # create an object to store info about Routine empty
        empty = data.Routine(
            name='empty',
            components=[hello],
        )
        empty.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for empty
        empty.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        empty.tStart = globalClock.getTime(format='float')
        empty.status = STARTED
        thisExp.addData('empty.started', empty.tStart)
        empty.maxDuration = None
        # keep track of which components have finished
        emptyComponents = empty.components
        for thisComponent in empty.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "empty" ---
        thisExp.currentRoutine = empty
        empty.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hello* updates
            
            # if hello is starting this frame...
            if hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hello.frameNStart = frameN  # exact frame index
                hello.tStart = t  # local t and not account for scr refresh
                hello.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hello, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hello.started')
                # update status
                hello.status = STARTED
                hello.setAutoDraw(True)
            
            # if hello is active this frame...
            if hello.status == STARTED:
                # update params
                pass
            
            # if hello is stopping this frame...
            if hello.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hello.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    hello.tStop = t  # not accounting for scr refresh
                    hello.tStopRefresh = tThisFlipGlobal  # on global time
                    hello.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'hello.stopped')
                    # update status
                    hello.status = FINISHED
                    hello.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=empty,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                empty.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if empty.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in empty.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "empty" ---
        for thisComponent in empty.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for empty
        empty.tStop = globalClock.getTime(format='float')
        empty.tStopRefresh = tThisFlipGlobal
        thisExp.addData('empty.stopped', empty.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if empty.maxDurationReached:
            routineTimer.addTime(-empty.maxDuration)
        elif empty.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "end_prac" ---
        # create an object to store info about Routine end_prac
        end_prac = data.Routine(
            name='end_prac',
            components=[],
        )
        end_prac.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        if prac1.thisN == 6:
            prac1.finished = True
        # store start times for end_prac
        end_prac.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        end_prac.tStart = globalClock.getTime(format='float')
        end_prac.status = STARTED
        thisExp.addData('end_prac.started', end_prac.tStart)
        end_prac.maxDuration = None
        # keep track of which components have finished
        end_pracComponents = end_prac.components
        for thisComponent in end_prac.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "end_prac" ---
        thisExp.currentRoutine = end_prac
        end_prac.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPrac1, 'status') and thisPrac1.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=end_prac,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                end_prac.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if end_prac.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in end_prac.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end_prac" ---
        for thisComponent in end_prac.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for end_prac
        end_prac.tStop = globalClock.getTime(format='float')
        end_prac.tStopRefresh = tThisFlipGlobal
        thisExp.addData('end_prac.stopped', end_prac.tStop)
        # the Routine "end_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisPrac1 as finished
        if hasattr(thisPrac1, 'status'):
            thisPrac1.status = FINISHED
        # if awaiting a pause, pause now
        if prac1.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            prac1.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac1'
    prac1.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "before_main" ---
    # create an object to store info about Routine before_main
    before_main = data.Routine(
        name='before_main',
        components=[image_4, key_resp_7, text_7],
    )
    before_main.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_7
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # Run 'Begin Routine' code from code_14
    total_w = 0
    # store start times for before_main
    before_main.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    before_main.tStart = globalClock.getTime(format='float')
    before_main.status = STARTED
    thisExp.addData('before_main.started', before_main.tStart)
    before_main.maxDuration = None
    # keep track of which components have finished
    before_mainComponents = before_main.components
    for thisComponent in before_main.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "before_main" ---
    thisExp.currentRoutine = before_main
    before_main.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        
        # if image_4 is starting this frame...
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            # update status
            image_4.status = STARTED
            image_4.setAutoDraw(True)
        
        # if image_4 is active this frame...
        if image_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_7* updates
        waitOnFlip = False
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=before_main,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            before_main.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if before_main.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in before_main.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "before_main" ---
    for thisComponent in before_main.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for before_main
    before_main.tStop = globalClock.getTime(format='float')
    before_main.tStopRefresh = tThisFlipGlobal
    thisExp.addData('before_main.stopped', before_main.tStop)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    thisExp.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        thisExp.addData('key_resp_7.rt', key_resp_7.rt)
        thisExp.addData('key_resp_7.duration', key_resp_7.duration)
    thisExp.nextEntry()
    # the Routine "before_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    main_session = data.TrialHandler2(
        name='main_session',
        nReps=3.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('cond_file.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(main_session)  # add the loop to the experiment
    thisMain_session = main_session.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_session.rgb)
    if thisMain_session != None:
        for paramName in thisMain_session:
            globals()[paramName] = thisMain_session[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMain_session in main_session:
        main_session.status = STARTED
        if hasattr(thisMain_session, 'status'):
            thisMain_session.status = STARTED
        currentLoop = main_session
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMain_session.rgb)
        if thisMain_session != None:
            for paramName in thisMain_session:
                globals()[paramName] = thisMain_session[paramName]
        
        # --- Prepare to start Routine "main_magic" ---
        # create an object to store info about Routine main_magic
        main_magic = data.Routine(
            name='main_magic',
            components=[],
        )
        main_magic.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_15
        current_session = main_session
        # store start times for main_magic
        main_magic.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        main_magic.tStart = globalClock.getTime(format='float')
        main_magic.status = STARTED
        thisExp.addData('main_magic.started', main_magic.tStart)
        main_magic.maxDuration = None
        # keep track of which components have finished
        main_magicComponents = main_magic.components
        for thisComponent in main_magic.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "main_magic" ---
        thisExp.currentRoutine = main_magic
        main_magic.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=main_magic,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                main_magic.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if main_magic.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in main_magic.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_magic" ---
        for thisComponent in main_magic.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for main_magic
        main_magic.tStop = globalClock.getTime(format='float')
        main_magic.tStopRefresh = tThisFlipGlobal
        thisExp.addData('main_magic.stopped', main_magic.tStop)
        # the Routine "main_magic" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_2],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            reference_line.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "sti_present" ---
        # create an object to store info about Routine sti_present
        sti_present = data.Routine(
            name='sti_present',
            components=[key_resp],
        )
        sti_present.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from present_bars
        #sti_base_type = 0
        #sti_cluster_number = 1
        #sample_size = 20
        #scale = 3 # if you are going to jitter the mean, take care!
        mouse.setVisible(0)
        small_bars = visual.ElementArrayStim(
                win=win,
                nElements=exp_general['n_dots_per_fresh'],
                elementTex=np.ones([16, 16]),
                elementMask="circle",
                sfs=0,
                xys=np.zeros((exp_general['n_dots_per_fresh'],2)),
                sizes=[exp_general['sample_circ_width'], exp_general['sample_circ_width']],
                oris=0, units='height', opacities=exp_general['sample_alpha'],colors = [1,-1,-1])
        
        my_overall_mean_jitter = (np.random.random()-0.5)*2*0.2
        
        weights_of_sampler = np.array(wms_dic[sti_base_type][sti_cluster_number]['w'])
        means_of_sampler = np.array(wms_dic[sti_base_type][sti_cluster_number]['m'])  + my_overall_mean_jitter
        sds_of_sampler = np.array(wms_dic[sti_base_type][sti_cluster_number]['s']) 
        
        my_stimulus = bounded_mixture_rvs(weights_of_sampler, 
                                  means_of_sampler,
                                  sds_of_sampler, sample_size, (my_overall_mean_jitter- 3 * 0.2, my_overall_mean_jitter+ 3 * 0.2))
        
        my_stimulus = my_stimulus.reshape((-1,exp_general['n_dots_per_fresh']))
        current_session.addData('sti', my_stimulus)
        current_session.addData('my_true_luster_mean', means_of_sampler)
        
        
        #画一下真实分布PDF做测试参考
        mix_pdf = gen_mixture_pdf(weights_of_sampler,means_of_sampler,sds_of_sampler)
        x_axis = np.linspace(-0.5,0.5,50)
        pdf_points = [(x,mix_pdf(x)*0.2-0.2) for x in x_axis]
        debug_curve = visual.ShapeStim(win,vertices = pdf_points,lineColor = "blue",closeShape = False)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for sti_present
        sti_present.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        sti_present.tStart = globalClock.getTime(format='float')
        sti_present.status = STARTED
        thisExp.addData('sti_present.started', sti_present.tStart)
        sti_present.maxDuration = None
        # keep track of which components have finished
        sti_presentComponents = sti_present.components
        for thisComponent in sti_present.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "sti_present" ---
        thisExp.currentRoutine = sti_present
        sti_present.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from present_bars
            reference_line.draw()
            #计算刺激呈现周期
            index_with_in_big_refresh = frameN % (exp_general['n_frame_per_fresh'] + exp_general['n_frame_per_empty'])
            if math.floor(index_with_in_big_refresh/exp_general['n_frame_per_fresh']) == 0:
            #应该亮起的帧数
            #每个火山石10帧（167ms）
                if index_with_in_big_refresh % exp_general['n_frame_per_fresh'] == 0: # Set the new samples to their location
                    row_index = math.floor(frameN/(exp_general['n_frame_per_fresh'] + exp_general['n_frame_per_empty']))
                    current_sti = my_stimulus[row_index, :]
                    new_position = np.array([current_sti, np.ones(exp_general['n_dots_per_fresh']) * y_of_the_axis_line+exp_general['sample_circ_width']/2, ]).T
                    small_bars.xys = new_position
                small_bars.draw()
            else: 
            #空白帧数
                if row_index == my_stimulus.shape[0]-1:
                    continueRoutine = False
                    
            
            #debug curve
            debug_curve.draw()
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=sti_present,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                sti_present.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if sti_present.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in sti_present.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "sti_present" ---
        for thisComponent in sti_present.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for sti_present
        sti_present.tStop = globalClock.getTime(format='float')
        sti_present.tStopRefresh = tThisFlipGlobal
        thisExp.addData('sti_present.stopped', sti_present.tStop)
        # the Routine "sti_present" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_2],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            reference_line.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "reproduction" ---
        # create an object to store info about Routine reproduction
        reproduction = data.Routine(
            name='reproduction',
            components=[mouse],
        )
        reproduction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code
        current_state = 'determine_cluster_mean'
        mouse.setVisible(1)
        mouse.setPos((np.random.random()-0.5, y_of_the_axis_line))
        pos = mouse.getPos()
        key_resp = keyboard.Keyboard()
        mean_choice_rts = []
        mean_choices = []
        
        cluster_choice_order_list = []
        cluster_choice_rt_list = []
        
        height_sd_order_list = []
        height_sd_time_list = []
        
        #画分布线，在横轴上取很多点
        x = np.concatenate((np.array([-5]),np.linspace(-1,+1,1001), np.array([5])))
        
        #一阶段瞄准线
        my_mean_estimation_bar = visual.rect.Rect(win = win, width = mean_bar_width, height = mean_bar_height, lineColor  = 'white',lineWidth =2,
                          units = 'height', fillColor = 'white', pos = (pos[0], y_of_the_axis_line))
        
        height_bar_width = 0.005
        height_bar_height = 0
        
        #综合概率包络线
        overall_line = visual.ShapeStim(
                win=win,
                lineColor='#0066CC',
                closeShape=False, units = 'height', lineWidth = 6, fillColor = 'white',
                opacity = 0.5,vertices = [[0,0]])
        
        #
        mean_bar_list = []
        
        pdf_line_list = []
        height_bar_list = []
        width_bar_list = []
        
        width_bar_left_cap_list = []
        width_bar_right_cap_list = []
        
        left_button_have_been_clicked = False
        
        #指导语
        rep_instruction = visual.TextStim(win,text = "单击鼠标左键选择火山位置，按f提交\n单击火山调整火山的范围及权重\n按Enter提交",
        pos = (-0.72,0.38),height = 0.05,color = "white",font = "SimHei",alignHoriz = "left",wrapWidth = 0.3)
        # store start times for reproduction
        reproduction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reproduction.tStart = globalClock.getTime(format='float')
        reproduction.status = STARTED
        thisExp.addData('reproduction.started', reproduction.tStart)
        reproduction.maxDuration = None
        # keep track of which components have finished
        reproductionComponents = reproduction.components
        for thisComponent in reproduction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reproduction" ---
        thisExp.currentRoutine = reproduction
        reproduction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse.prevButtonState = mouse.getPressed()
            # Run 'Each Frame' code from code
            keys = key_resp.getKeys(keyList=['f', 'return'])
            pos = mouse.getPos()
            clicked_buttons, click_time = mouse.getPressed(getTime = True)
            left_button_clicked = clicked_buttons[0]
            #一阶段：找到火山
            if current_state == 'determine_cluster_mean': # In this stage, participants need to use mouse to mark the location of different cluster centers
                my_mean_estimation_bar.pos = (pos[0], y_of_the_axis_line)
                if left_button_clicked:
                    left_button_have_been_clicked = True
                #检测鼠标松开的瞬间
                elif (left_button_clicked == 0) and left_button_have_been_clicked:
                    #防止火山重叠
                    if np.all(np.abs(np.array(mean_choices) - pos[0]) > mean_bar_height/2):
                        left_button_have_been_clicked = False
                        #记录点击位置和时间
                        mean_choice_rts.append(t)
                        mean_choices.append(pos[0])
                        my_mean_bar = visual.ImageStim(
                    win=win,
                    image='volcano.png', mask=None,
                    ori=0.0, pos=(pos[0], y_of_the_axis_line+mean_bar_height/2), size=(mean_bar_height, mean_bar_height),
                    color=[1,1,1], colorSpace='rgb', opacity=0.4,
                    flipHoriz=False, flipVert=False,units = 'height',
                    texRes=128.0, interpolate=True, depth=-1.0)
                        mean_bar_list.append(my_mean_bar)
                    else:
                        left_button_have_been_clicked = False
            
                elif len(keys) > 0 and len(mean_choices)>=1:
                    pressed_key = keys[0]
                        
                    if pressed_key == 'f':
                        #结束找火山，等待被试选择估计哪个火山的范围和权重
                        left_button_have_been_clicked = False
                        current_state = 'determin_which_cluster_to_assign_weight_and_SD'
                        num_clusters = len(mean_bar_list)
            
                        height_list = [0] * num_clusters
                        sd_list = [0.005] * num_clusters
                        mean_list = [i.pos[0] for i in mean_bar_list]
                        
                        #建立一些有待后续使用的神秘对象
                        pdf_line_list = [visual.ShapeStim(win=win,lineColor='white',closeShape=False, 
                                         units = 'height', lineWidth = 3, fillColor = 'white',opacity = 0.5,vertices = [[0,0]])
                                         for i in range(num_clusters)]
                        height_bar_list = [visual.rect.Rect(win = win, width = height_bar_width, height = 0, lineColor = '#0066CC',lineWidth =2,
                                           units = 'height', fillColor = '#0066CC', pos = (m,y_of_the_axis_line)) for m in mean_list]
            
                        width_bar_list = [visual.rect.Rect(win = win, width = 0, height = 0.002, lineColor  = '#FF9900',lineWidth =0,
                                           units = 'height', fillColor = '#FF9900', pos = (m,y_of_the_axis_line), opacity = 0.5) for m in mean_list]
                                           
                        width_bar_left_cap_list = [visual.rect.Rect(win = win, width = 0.002, height = 0.03, lineColor  = '#FF9900',lineWidth =0,
                                           units = 'height', fillColor = '#FF9900', pos = (m,y_of_the_axis_line), opacity = 0.5) for m in mean_list]
                        width_bar_right_cap_list = [visual.rect.Rect(win = win, width = 0.002, height = 0.03, lineColor  = '#FF9900',lineWidth =0,
                                           units = 'height', fillColor = '#FF9900', pos = (m,y_of_the_axis_line), opacity = 0.5) for m in mean_list]
            
                        mouse.setVisible(1)
                        #隐藏瞄准线
                        my_mean_estimation_bar.opacity = 0
            
            elif current_state == 'determin_which_cluster_to_assign_weight_and_SD': # In this stage, participants need to click the white mean bar and enter the 'adjuct_weight_and_SD' stage
                for bar_index, current_bar in enumerate(mean_bar_list):
                    #如果被试点击了某一个火山
                    if mouse.isPressedIn(current_bar):
                        left_button_have_been_clicked = True
                        selected_index = bar_index
                    elif (left_button_clicked == 0) and left_button_have_been_clicked and selected_index == bar_index:
                        left_button_have_been_clicked = False
                        
                        #取出刚刚表格中对应对象
                        my_line = pdf_line_list[bar_index]
                        current_height_bar = height_bar_list[bar_index]
                        current_width_bar = width_bar_list[bar_index]
                        current_state = 'adjuct_weight_and_SD'
                        mean_of_the_cluster = mean_choices[bar_index]
                        width_bar_left_cap = width_bar_left_cap_list[bar_index]
                        width_bar_right_cap = width_bar_right_cap_list[bar_index]
                        
                        #让选中的火山亮起
                        current_bar.opacity = 1
                        selected_index = bar_index
                        
                        cluster_choice_order_list.append(selected_index)
                        cluster_choice_rt_list.append(t)
                        
                #调完之后提交
                if len(keys) > 0: 
                    pressed_key = keys[0]
                    if pressed_key == 'return' and np.all([i.opacity == 1 for i in mean_bar_list]):
                        continueRoutine = False
                        current_session.addData('mean_list', mean_list)#每个火山的位置
                        current_session.addData('height_list', height_list)#每个火山分布的中心高度
                        current_session.addData('sd_list', sd_list)#每个火山分布的标准差
                        current_session.addData('mean_click_rt', mean_choice_rts)
                        current_session.addData('cluster_choice_order_list', cluster_choice_order_list)
                        current_session.addData('cluster_choice_rt_list', cluster_choice_rt_list)
                        current_session.addData('height_sd_order_list', height_sd_order_list)
                        current_session.addData('height_sd_time_list', height_sd_time_list)
                        
            
            elif current_state == 'adjuct_weight_and_SD': # In this stage, participants need to adjust the weight and SD of the selected cluster
                my_width = np.max([0.005,np.abs(pos[0]-mean_of_the_cluster)]) # take care! it's 65% area!!
                my_std = my_width/0.934
                my_height = np.max([0, pos[1]-y_of_the_axis_line])
                dist_height_scale_factor = norm.pdf(0, loc = 0, scale = my_std)
                
                
                
                sd_list[selected_index] = my_std
                height_list[selected_index] = my_height
                
                #更改大包络线的设置
                all_heights = np.array([norm.pdf(x, loc = mean_list[i], scale = sd_list[i])* height_list[i]/norm.pdf(0, loc = 0, scale = sd_list[i]) for i in range(num_clusters)])
                sumed_heights = np.sum(all_heights, axis = 0)
                normalizing_factor = 1
                sumed_heights = sumed_heights / normalizing_factor
                overall_y = sumed_heights + y_of_the_axis_line
                overall_line.vertices = np.array((x, overall_y)).T
                
                #画当前火山的分布线
                current_height_bar.height = my_height
                current_height_bar.pos = [mean_of_the_cluster, y_of_the_axis_line + my_height/2]
                current_width_bar.width = my_width*2
                
                width_bar_left_cap.pos = [mean_of_the_cluster-my_width, y_of_the_axis_line]
                width_bar_right_cap.pos = [mean_of_the_cluster+my_width, y_of_the_axis_line]
                
                
                y = norm.pdf(x, loc = mean_of_the_cluster, scale = my_std) * my_height/dist_height_scale_factor+y_of_the_axis_line
                my_line.vertices = np.array((x,y)).T
                my_line.closeShape = True
                my_line.draw()
                
                #let's try it
                #current_width_bar.draw()
                #width_bar_left_cap.draw()
                #current_height_bar.draw()
                
                #完成一个火山之后返回等待状态
                if left_button_clicked:
                    left_button_have_been_clicked = True
                elif (left_button_clicked == 0) and left_button_have_been_clicked:
                    height_list[selected_index] = my_height
                    sd_list[selected_index] = my_std
                    
                    height_sd_order_list.append([my_height, my_std])
                    height_sd_time_list.append(t)
                    
                    left_button_have_been_clicked = False
                    current_state = 'determin_which_cluster_to_assign_weight_and_SD'
            
            
            #轴线
            reference_line.draw()
            
            
            #画出所有火山
            for i in mean_bar_list:
                i.draw()
                
            #画总分布线
            overall_line.draw()
            
            #瞄准线
            my_mean_estimation_bar.draw()
            
            #显示指导语
            rep_instruction.draw()
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=reproduction,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                reproduction.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if reproduction.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in reproduction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reproduction" ---
        for thisComponent in reproduction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reproduction
        reproduction.tStop = globalClock.getTime(format='float')
        reproduction.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reproduction.stopped', reproduction.tStop)
        # store data for main_session (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        main_session.addData('mouse.x', x)
        main_session.addData('mouse.y', y)
        main_session.addData('mouse.leftButton', buttons[0])
        main_session.addData('mouse.midButton', buttons[1])
        main_session.addData('mouse.rightButton', buttons[2])
        # the Routine "reproduction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "normalization" ---
        # create an object to store info about Routine normalization
        normalization = data.Routine(
            name='normalization',
            components=[text],
        )
        normalization.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        overall_line = visual.ShapeStim(
                win=win,
                lineColor='#0066CC',
                closeShape=False, units = 'height', lineWidth = 6, fillColor = 'white',
                opacity = 0.5,vertices = [[0,0]])
        x = np.concatenate((np.array([-5]),np.linspace(-1,+1,1001), np.array([5])))
        #对每个火山，计算每个点的高度，所有火山加和形成总包络线
        #all_heights:每一行是一座火山，K行*1001列
        all_heights = np.array([my_pdf_line.vertices[:,1]-y_of_the_axis_line for my_pdf_line in pdf_line_list])
        sumed_heights = np.sum(all_heights, axis = 0)#把每一列加和，得到1*1001
        normalizing_factor = 1 # ?历史遗留问题
        sumed_heights = sumed_heights / normalizing_factor
        overall_y = sumed_heights + y_of_the_axis_line
        overall_line.vertices = np.array((x, overall_y)).T
        
        
        weight_list = np.sum(all_heights, axis = 1)/ np.sum(sumed_heights)#axis = 1:把每一行加和，得到单个火山下的面积
        current_session.addData('weight_list', weight_list)#得到权重分配
        
        #也是历史遗留问题
        for i in pdf_line_list:
            i.vertices = np.array((x, (i.vertices[:, -1] - y_of_the_axis_line) / normalizing_factor+ y_of_the_axis_line)).T
        
        #用真实分布和被试报告的分布分别取样，计算wasserstein距离，评价作答准确性
        u_dist = bounded_mixture_rvs(weights_of_sampler, 
                                  means_of_sampler,
                                  sds_of_sampler, 10000,(my_overall_mean_jitter- 2.8 * 0.2, my_overall_mean_jitter+ 2.8 * 0.2))
        
        v_dist = bounded_mixture_rvs(weight_list, 
                                  mean_list,
                                  sd_list, 10000,(my_overall_mean_jitter- 2.8 * 0.2, my_overall_mean_jitter+ 2.8 * 0.2))
        
        w_distance = wasserstein_distance(u_dist, v_dist)
        total_w += w_distance
        current_session.addData('w_distance', w_distance)
        
        
        my_stimulus = my_stimulus.reshape(-1)
        #展示真实曲线和真实刺激点？不需要
        feedback_line = visual.ShapeStim(
                win=win,
                lineColor='green',
                closeShape=False, units = 'height', lineWidth = 6, fillColor = 'white',
                opacity = 0.5,vertices = [[0,0]])
        my_pdf = gen_mixture_pdf(weights_of_sampler, 
                                  means_of_sampler,
                                  sds_of_sampler)
        feedback_height = np.sum(sumed_heights) * my_pdf(x)/np.sum(my_pdf(x))+y_of_the_axis_line
        feedback_line.vertices = np.array((x, feedback_height)).T
        
        my_stimulus = my_stimulus.reshape(-1)
        feedback_dots = visual.ElementArrayStim(
                win=win,
                nElements=sample_size,
                elementTex=np.ones([16, 16]),
                elementMask="circle",
                sfs=0,
                xys=np.array((my_stimulus, y_of_the_axis_line + (np.random.random(sample_size)-0.5)/100)).T,
                sizes=[exp_general['sample_circ_width'], exp_general['sample_circ_width']],
                oris=0, units='height', opacities=0.3,colors = [1,-1,-1])
        # store start times for normalization
        normalization.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        normalization.tStart = globalClock.getTime(format='float')
        normalization.status = STARTED
        thisExp.addData('normalization.started', normalization.tStart)
        normalization.maxDuration = None
        # keep track of which components have finished
        normalizationComponents = normalization.components
        for thisComponent in normalization.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "normalization" ---
        thisExp.currentRoutine = normalization
        normalization.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            #每个火山的分布线
            for i in pdf_line_list:
                i.draw()
            #总和分布线
            overall_line.draw()
            
            #画所有火山
            for i in mean_bar_list:
                i.draw()
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=normalization,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                normalization.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if normalization.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in normalization.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "normalization" ---
        for thisComponent in normalization.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for normalization
        normalization.tStop = globalClock.getTime(format='float')
        normalization.tStopRefresh = tThisFlipGlobal
        thisExp.addData('normalization.stopped', normalization.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if normalization.maxDurationReached:
            routineTimer.addTime(-normalization.maxDuration)
        elif normalization.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "empty" ---
        # create an object to store info about Routine empty
        empty = data.Routine(
            name='empty',
            components=[hello],
        )
        empty.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for empty
        empty.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        empty.tStart = globalClock.getTime(format='float')
        empty.status = STARTED
        thisExp.addData('empty.started', empty.tStart)
        empty.maxDuration = None
        # keep track of which components have finished
        emptyComponents = empty.components
        for thisComponent in empty.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "empty" ---
        thisExp.currentRoutine = empty
        empty.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hello* updates
            
            # if hello is starting this frame...
            if hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hello.frameNStart = frameN  # exact frame index
                hello.tStart = t  # local t and not account for scr refresh
                hello.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hello, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hello.started')
                # update status
                hello.status = STARTED
                hello.setAutoDraw(True)
            
            # if hello is active this frame...
            if hello.status == STARTED:
                # update params
                pass
            
            # if hello is stopping this frame...
            if hello.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hello.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    hello.tStop = t  # not accounting for scr refresh
                    hello.tStopRefresh = tThisFlipGlobal  # on global time
                    hello.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'hello.stopped')
                    # update status
                    hello.status = FINISHED
                    hello.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=empty,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                empty.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if empty.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in empty.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "empty" ---
        for thisComponent in empty.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for empty
        empty.tStop = globalClock.getTime(format='float')
        empty.tStopRefresh = tThisFlipGlobal
        thisExp.addData('empty.stopped', empty.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if empty.maxDurationReached:
            routineTimer.addTime(-empty.maxDuration)
        elif empty.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "inter_block_rest" ---
        # create an object to store info about Routine inter_block_rest
        inter_block_rest = data.Routine(
            name='inter_block_rest',
            components=[text_4],
        )
        inter_block_rest.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_7
        
        rest_text  = ' '
        if main_session.thisN in rest_trials:
        
            finished_block_number = main_session.thisN/rest_trials[0]
            rest_time = 30
            rest_text = '本组块结束！\n已经完成了{}个组快。本实验一共有{}个组块\n请休息30秒！'.format(finished_block_number,num_blocks)
        
        else:
            rest_time = 0
            rest_text = ' '
        text_4.setText(rest_text)
        # store start times for inter_block_rest
        inter_block_rest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        inter_block_rest.tStart = globalClock.getTime(format='float')
        inter_block_rest.status = STARTED
        thisExp.addData('inter_block_rest.started', inter_block_rest.tStart)
        inter_block_rest.maxDuration = None
        # keep track of which components have finished
        inter_block_restComponents = inter_block_rest.components
        for thisComponent in inter_block_rest.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "inter_block_rest" ---
        thisExp.currentRoutine = inter_block_rest
        inter_block_rest.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # if text_4 is stopping this frame...
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + rest_time-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.tStopRefresh = tThisFlipGlobal  # on global time
                    text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.stopped')
                    # update status
                    text_4.status = FINISHED
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=inter_block_rest,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                inter_block_rest.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if inter_block_rest.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in inter_block_rest.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inter_block_rest" ---
        for thisComponent in inter_block_rest.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for inter_block_rest
        inter_block_rest.tStop = globalClock.getTime(format='float')
        inter_block_rest.tStopRefresh = tThisFlipGlobal
        thisExp.addData('inter_block_rest.stopped', inter_block_rest.tStop)
        # the Routine "inter_block_rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "space_to_start" ---
        # create an object to store info about Routine space_to_start
        space_to_start = data.Routine(
            name='space_to_start',
            components=[key_resp_5, text_5],
        )
        space_to_start.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_8
        #if main_session.thisN == 2:
        #    main_session.finished = True
        
        if main_session.thisN not in rest_trials:
           continueRoutine = False
            
            
        # create starting attributes for key_resp_5
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # store start times for space_to_start
        space_to_start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        space_to_start.tStart = globalClock.getTime(format='float')
        space_to_start.status = STARTED
        thisExp.addData('space_to_start.started', space_to_start.tStart)
        space_to_start.maxDuration = None
        # keep track of which components have finished
        space_to_startComponents = space_to_start.components
        for thisComponent in space_to_start.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "space_to_start" ---
        thisExp.currentRoutine = space_to_start
        space_to_start.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_session, 'status') and thisMain_session.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=space_to_start,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                space_to_start.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if space_to_start.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in space_to_start.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "space_to_start" ---
        for thisComponent in space_to_start.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for space_to_start
        space_to_start.tStop = globalClock.getTime(format='float')
        space_to_start.tStopRefresh = tThisFlipGlobal
        thisExp.addData('space_to_start.stopped', space_to_start.tStop)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        main_session.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            main_session.addData('key_resp_5.rt', key_resp_5.rt)
            main_session.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "space_to_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisMain_session as finished
        if hasattr(thisMain_session, 'status'):
            thisMain_session.status = FINISHED
        # if awaiting a pause, pause now
        if main_session.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            main_session.status = STARTED
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'main_session'
    main_session.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[text_6, key_resp_6],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_9
    
    total_distance = total_w
    total_reward = np.max([0,72*2*0.29 - total_distance])
    
    last_msg = '实验结束了！你一共得到了{}个奖励点。'.format(total_reward)
    text_6.setText(last_msg)
    # create starting attributes for key_resp_6
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    thisExp.currentRoutine = end
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['e'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=end,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            end.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if end.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
