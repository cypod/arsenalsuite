# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_export/ui/DirectoryUI.ui'
#
# Created: Fri Oct  9 09:27:08 2009
#      by: PyQt4 UI code generator 4.5-snapshot-20090412
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DirectoryImport(object):
    def setupUi(self, DirectoryImport):
        DirectoryImport.setObjectName("DirectoryImport")
        DirectoryImport.resize(1042, 855)
        self.centralwidget = QtGui.QWidget(DirectoryImport)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mDirectory = QtGui.QLineEdit(self.widget)
        self.mDirectory.setObjectName("mDirectory")
        self.horizontalLayout.addWidget(self.mDirectory)
        self.mDirectoryChoose = QtGui.QPushButton(self.widget)
        self.mDirectoryChoose.setObjectName("mDirectoryChoose")
        self.horizontalLayout.addWidget(self.mDirectoryChoose)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mDoSubdirsCB = QtGui.QCheckBox(self.widget_2)
        self.mDoSubdirsCB.setObjectName("mDoSubdirsCB")
        self.horizontalLayout_2.addWidget(self.mDoSubdirsCB)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.mGatherFilesBtn = QtGui.QPushButton(self.widget_2)
        self.mGatherFilesBtn.setObjectName("mGatherFilesBtn")
        self.horizontalLayout_2.addWidget(self.mGatherFilesBtn)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mSelectAllButton = QtGui.QPushButton(self.centralwidget)
        self.mSelectAllButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.mSelectAllButton.setObjectName("mSelectAllButton")
        self.horizontalLayout_4.addWidget(self.mSelectAllButton)
        self.mSelectNoneButton = QtGui.QPushButton(self.centralwidget)
        self.mSelectNoneButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.mSelectNoneButton.setObjectName("mSelectNoneButton")
        self.horizontalLayout_4.addWidget(self.mSelectNoneButton)
        self.mToggleButton = QtGui.QPushButton(self.centralwidget)
        self.mToggleButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.mToggleButton.setObjectName("mToggleButton")
        self.horizontalLayout_4.addWidget(self.mToggleButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.mFileTree = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mFileTree.sizePolicy().hasHeightForWidth())
        self.mFileTree.setSizePolicy(sizePolicy)
        self.mFileTree.setMinimumSize(QtCore.QSize(0, 0))
        self.mFileTree.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mFileTree.setAlternatingRowColors(True)
        self.mFileTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.mFileTree.setRootIsDecorated(False)
        self.mFileTree.setObjectName("mFileTree")
        self.log = QtGui.QPlainTextEdit(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setMinimumSize(QtCore.QSize(0, 0))
        self.log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        self.log.setFont(font)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.mTagEdit = QtGui.QLineEdit(self.centralwidget)
        self.mTagEdit.setObjectName("mTagEdit")
        self.horizontalLayout_5.addWidget(self.mTagEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.mImportBtn = QtGui.QPushButton(self.widget_3)
        self.mImportBtn.setObjectName("mImportBtn")
        self.horizontalLayout_3.addWidget(self.mImportBtn)
        self.verticalLayout.addWidget(self.widget_3)
        DirectoryImport.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(DirectoryImport)
        self.statusBar.setObjectName("statusBar")
        DirectoryImport.setStatusBar(self.statusBar)

        self.retranslateUi(DirectoryImport)
        QtCore.QMetaObject.connectSlotsByName(DirectoryImport)

    def retranslateUi(self, DirectoryImport):
        DirectoryImport.setWindowTitle(QtGui.QApplication.translate("DirectoryImport", "Bach Directory Import", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DirectoryImport", "Import Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.mDirectoryChoose.setText(QtGui.QApplication.translate("DirectoryImport", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.mDoSubdirsCB.setText(QtGui.QApplication.translate("DirectoryImport", "Do Subdirectories", None, QtGui.QApplication.UnicodeUTF8))
        self.mGatherFilesBtn.setText(QtGui.QApplication.translate("DirectoryImport", "Gather Files", None, QtGui.QApplication.UnicodeUTF8))
        self.mSelectAllButton.setText(QtGui.QApplication.translate("DirectoryImport", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.mSelectNoneButton.setText(QtGui.QApplication.translate("DirectoryImport", "Select None", None, QtGui.QApplication.UnicodeUTF8))
        self.mToggleButton.setText(QtGui.QApplication.translate("DirectoryImport", "Toggle Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.mFileTree.setSortingEnabled(True)
        self.mFileTree.headerItem().setText(0, QtGui.QApplication.translate("DirectoryImport", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.mFileTree.headerItem().setText(1, QtGui.QApplication.translate("DirectoryImport", "Exists", None, QtGui.QApplication.UnicodeUTF8))
        self.mFileTree.headerItem().setText(2, QtGui.QApplication.translate("DirectoryImport", "Excluded", None, QtGui.QApplication.UnicodeUTF8))
        self.mFileTree.headerItem().setText(3, QtGui.QApplication.translate("DirectoryImport", "Old Path", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DirectoryImport", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.mTagEdit.setToolTip(QtGui.QApplication.translate("DirectoryImport", "comma separated list of tags for imported items", None, QtGui.QApplication.UnicodeUTF8))
        self.mImportBtn.setText(QtGui.QApplication.translate("DirectoryImport", "Import", None, QtGui.QApplication.UnicodeUTF8))

