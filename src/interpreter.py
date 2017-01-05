"""
    bin/interpreter.py
    ------------------

    Runs a block of FoxDot code. Designed to be overloaded
    for other language communication

"""
# Option 1: only requiring a clock

from config import *
import time

class Clock:
    def __init__(self):
        self.time = 0
        self.mark = time.time()
    def kill(self):
        return
    def reset(self):
        self.time = 0
        self.mark = time.time()
    def settime(self, t):
        self.time = t
    def now(self):
        now = time.time()
        self.time += now - self.mark
        self.mark = now
        return self.time

class EmptyInterpreter(Clock):
    lang = None
    clock = None
    def evaluate(self, string):
        return 

# Option 2: FoxDot

class FoxDotInterpreter(EmptyInterpreter):
    def __init__(self):
        import FoxDot
        self.lang  = FoxDot
        self.clock = FoxDot.Clock
    def kill(self):
        self.clock.stop()
    def now(self):
        return self.clock.now()
    def settime(self, t):
        """ t is in seconds, sets clock time to  """
        bpm   = float(self.clock.bpm)
        beats = float(t) * (bpm / 60)
        now   = float(self.now())
        if beats < 0.95 * now or beats > 1.05 * now:
            self.clock.time = beats
    def evaluate(self, string):
        return self.lang.execute(string)

### Define

if LANGUAGE == FOXDOT:

    Interpreter = FoxDotInterpreter
    
        