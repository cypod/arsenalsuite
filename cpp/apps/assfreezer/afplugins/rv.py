
from blur.Stone import *
from blur.Classes import *
from blur.Assfreezer import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
import traceback, os
import subprocess

class RvViewerPlugin(JobViewerPlugin):
    def __init__(self):
        JobViewerPlugin.__init__(self)

    def name(self):
        return QString("rv")

    def icon(self):
        return QString("images/rv2.png")

    def view(self, jobList):
        for job in jobList:
            print "rv -l %s" % job.outputPath().replace("..",".#.")
            subprocess.Popen(["rv", "-l", job.outputPath().replace("..",".#.")])

JobViewerFactory.registerPlugin( RvViewerPlugin() )

