# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lix/GoProjects/Dict2Anki/Dict2Anki/addon/UIForm/mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 533)
        self.main_layout = QtWidgets.QVBoxLayout(Dialog)
        self.main_layout.setObjectName("main_layout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.mainTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnSync = QtWidgets.QPushButton(self.mainTab)
        self.btnSync.setEnabled(False)
        self.btnSync.setObjectName("btnSync")
        self.gridLayout_4.addWidget(self.btnSync, 4, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.newWordListWidget = QtWidgets.QListWidget(self.mainTab)
        self.newWordListWidget.setAlternatingRowColors(True)
        self.newWordListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.newWordListWidget.setObjectName("newWordListWidget")
        self.verticalLayout.addWidget(self.newWordListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.mainTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.needDeleteWordListWidget = QtWidgets.QListWidget(self.mainTab)
        self.needDeleteWordListWidget.setAlternatingRowColors(True)
        self.needDeleteWordListWidget.setObjectName("needDeleteWordListWidget")
        self.verticalLayout_2.addWidget(self.needDeleteWordListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 0, 1, 4)
        self.deckLayout = QtWidgets.QHBoxLayout()
        self.deckLayout.setObjectName("deckLayout")
        self.deckLabel = QtWidgets.QLabel(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckLabel.sizePolicy().hasHeightForWidth())
        self.deckLabel.setSizePolicy(sizePolicy)
        self.deckLabel.setObjectName("deckLabel")
        self.deckLayout.addWidget(self.deckLabel)
        self.deckComboBox = QtWidgets.QComboBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckComboBox.sizePolicy().hasHeightForWidth())
        self.deckComboBox.setSizePolicy(sizePolicy)
        self.deckComboBox.setEditable(True)
        self.deckComboBox.setObjectName("deckComboBox")
        self.deckLayout.addWidget(self.deckComboBox)
        self.gridLayout_4.addLayout(self.deckLayout, 0, 0, 1, 4)
        self.apiLayout = QtWidgets.QHBoxLayout()
        self.apiLayout.setObjectName("apiLayout")
        self.apiLabel = QtWidgets.QLabel(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiLabel.sizePolicy().hasHeightForWidth())
        self.apiLabel.setSizePolicy(sizePolicy)
        self.apiLabel.setObjectName("apiLabel")
        self.apiLayout.addWidget(self.apiLabel)
        self.apiComboBox = QtWidgets.QComboBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiComboBox.sizePolicy().hasHeightForWidth())
        self.apiComboBox.setSizePolicy(sizePolicy)
        self.apiComboBox.setObjectName("apiComboBox")
        self.apiLayout.addWidget(self.apiComboBox)
        self.gridLayout_4.addLayout(self.apiLayout, 2, 0, 1, 4)
        self.dictionaryLayout = QtWidgets.QHBoxLayout()
        self.dictionaryLayout.setObjectName("dictionaryLayout")
        self.dictionaryLabel = QtWidgets.QLabel(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionaryLabel.sizePolicy().hasHeightForWidth())
        self.dictionaryLabel.setSizePolicy(sizePolicy)
        self.dictionaryLabel.setObjectName("dictionaryLabel")
        self.dictionaryLayout.addWidget(self.dictionaryLabel)
        self.dictionaryComboBox = QtWidgets.QComboBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dictionaryComboBox.sizePolicy().hasHeightForWidth())
        self.dictionaryComboBox.setSizePolicy(sizePolicy)
        self.dictionaryComboBox.setObjectName("dictionaryComboBox")
        self.dictionaryLayout.addWidget(self.dictionaryComboBox)
        self.gridLayout_4.addLayout(self.dictionaryLayout, 1, 0, 1, 4)
        self.queryBtn = QtWidgets.QPushButton(self.mainTab)
        self.queryBtn.setEnabled(False)
        self.queryBtn.setObjectName("queryBtn")
        self.gridLayout_4.addWidget(self.queryBtn, 4, 1, 1, 1)
        self.pullRemoteWordsBtn = QtWidgets.QPushButton(self.mainTab)
        self.pullRemoteWordsBtn.setObjectName("pullRemoteWordsBtn")
        self.gridLayout_4.addWidget(self.pullRemoteWordsBtn, 4, 0, 1, 1)
        self.tabWidget.addTab(self.mainTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.defaultConfigGroupBox = QtWidgets.QGroupBox(self.settingTab)
        self.defaultConfigGroupBox.setObjectName("defaultConfigGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.defaultConfigGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.BrEPhoneticCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.BrEPhoneticCheckBox.setChecked(True)
        self.BrEPhoneticCheckBox.setObjectName("BrEPhoneticCheckBox")
        self.gridLayout.addWidget(self.BrEPhoneticCheckBox, 1, 1, 1, 1)
        self.imageCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.imageCheckBox.setChecked(True)
        self.imageCheckBox.setObjectName("imageCheckBox")
        self.gridLayout.addWidget(self.imageCheckBox, 1, 0, 1, 1)
        self.definitionCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.definitionCheckBox.setChecked(True)
        self.definitionCheckBox.setObjectName("definitionCheckBox")
        self.gridLayout.addWidget(self.definitionCheckBox, 0, 0, 1, 1)
        self.sentenceCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.sentenceCheckBox.setChecked(True)
        self.sentenceCheckBox.setObjectName("sentenceCheckBox")
        self.gridLayout.addWidget(self.sentenceCheckBox, 0, 2, 1, 1)
        self.phraseCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.phraseCheckBox.setChecked(True)
        self.phraseCheckBox.setObjectName("phraseCheckBox")
        self.gridLayout.addWidget(self.phraseCheckBox, 0, 1, 1, 1)
        self.AmEPhoneticCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.AmEPhoneticCheckBox.setChecked(True)
        self.AmEPhoneticCheckBox.setObjectName("AmEPhoneticCheckBox")
        self.gridLayout.addWidget(self.AmEPhoneticCheckBox, 1, 2, 1, 1)
        self.noPronRadioButton = QtWidgets.QRadioButton(self.defaultConfigGroupBox)
        self.noPronRadioButton.setEnabled(True)
        self.noPronRadioButton.setObjectName("noPronRadioButton")
        self.gridLayout.addWidget(self.noPronRadioButton, 5, 0, 1, 1)
        self.AmEPronRadioButton = QtWidgets.QRadioButton(self.defaultConfigGroupBox)
        self.AmEPronRadioButton.setChecked(True)
        self.AmEPronRadioButton.setObjectName("AmEPronRadioButton")
        self.gridLayout.addWidget(self.AmEPronRadioButton, 5, 2, 1, 1)
        self.BrEPronRadioButton = QtWidgets.QRadioButton(self.defaultConfigGroupBox)
        self.BrEPronRadioButton.setChecked(False)
        self.BrEPronRadioButton.setObjectName("BrEPronRadioButton")
        self.gridLayout.addWidget(self.BrEPronRadioButton, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.defaultConfigGroupBox, 1, 0, 1, 2)
        self.credentialGroupBox = QtWidgets.QGroupBox(self.settingTab)
        self.credentialGroupBox.setObjectName("credentialGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.credentialGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.currentDictionaryLabel = QtWidgets.QLabel(self.credentialGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentDictionaryLabel.sizePolicy().hasHeightForWidth())
        self.currentDictionaryLabel.setSizePolicy(sizePolicy)
        self.currentDictionaryLabel.setObjectName("currentDictionaryLabel")
        self.gridLayout_3.addWidget(self.currentDictionaryLabel, 0, 0, 1, 2)
        self.usernameLabel = QtWidgets.QLabel(self.credentialGroupBox)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout_3.addWidget(self.usernameLabel, 1, 0, 1, 1)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.credentialGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLineEdit.sizePolicy().hasHeightForWidth())
        self.usernameLineEdit.setSizePolicy(sizePolicy)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout_3.addWidget(self.usernameLineEdit, 1, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.credentialGroupBox)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout_3.addWidget(self.passwordLabel, 2, 0, 1, 1)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.credentialGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout_3.addWidget(self.passwordLineEdit, 2, 1, 1, 1)
        self.cookieLabel = QtWidgets.QLabel(self.credentialGroupBox)
        self.cookieLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cookieLabel.setObjectName("cookieLabel")
        self.gridLayout_3.addWidget(self.cookieLabel, 3, 0, 1, 1)
        self.cookieLineEdit = QtWidgets.QLineEdit(self.credentialGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookieLineEdit.sizePolicy().hasHeightForWidth())
        self.cookieLineEdit.setSizePolicy(sizePolicy)
        self.cookieLineEdit.setClearButtonEnabled(True)
        self.cookieLineEdit.setObjectName("cookieLineEdit")
        self.gridLayout_3.addWidget(self.cookieLineEdit, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.credentialGroupBox, 0, 0, 1, 2)
        self.tabWidget.addTab(self.settingTab, "")
        self.utilitiesTab = QtWidgets.QWidget()
        self.utilitiesTab.setObjectName("utilitiesTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.utilitiesTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.dangerZoneGroupBox = QtWidgets.QGroupBox(self.utilitiesTab)
        self.dangerZoneGroupBox.setStyleSheet("color: red")
        self.dangerZoneGroupBox.setObjectName("dangerZoneGroupBox")
        self.btnBackwardTemplate = QtWidgets.QPushButton(self.dangerZoneGroupBox)
        self.btnBackwardTemplate.setGeometry(QtCore.QRect(145, 29, 234, 32))
        self.btnBackwardTemplate.setObjectName("btnBackwardTemplate")
        self.gridLayout_5.addWidget(self.dangerZoneGroupBox, 1, 0, 1, 1)
        self.utilitiesGroupBox = QtWidgets.QGroupBox(self.utilitiesTab)
        self.utilitiesGroupBox.setObjectName("utilitiesGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.utilitiesGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.btnDownloadMissingAssets = QtWidgets.QPushButton(self.utilitiesGroupBox)
        self.btnDownloadMissingAssets.setObjectName("btnDownloadMissingAssets")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btnDownloadMissingAssets)
        self.btnExportAudio = QtWidgets.QPushButton(self.utilitiesGroupBox)
        self.btnExportAudio.setObjectName("btnExportAudio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btnExportAudio)
        self.gridLayout_5.addWidget(self.utilitiesGroupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.utilitiesTab, "")
        self.main_layout.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.main_layout.addWidget(self.progressBar)
        self.logTextBox = QtWidgets.QPlainTextEdit(Dialog)
        self.logTextBox.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.logTextBox.setObjectName("logTextBox")
        self.main_layout.addWidget(self.logTextBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSync.setText(_translate("Dialog", "Sync"))
        self.label.setText(_translate("Dialog", "新单词"))
        self.label_2.setText(_translate("Dialog", "待删除"))
        self.deckLabel.setText(_translate("Dialog", "牌组"))
        self.apiLabel.setText(_translate("Dialog", "查询"))
        self.dictionaryLabel.setText(_translate("Dialog", "词典"))
        self.queryBtn.setText(_translate("Dialog", "Query"))
        self.pullRemoteWordsBtn.setText(_translate("Dialog", "Pull words"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Dialog", "同步"))
        self.defaultConfigGroupBox.setTitle(_translate("Dialog", "默认设置"))
        self.BrEPhoneticCheckBox.setText(_translate("Dialog", "英式英标"))
        self.imageCheckBox.setText(_translate("Dialog", "图片"))
        self.definitionCheckBox.setText(_translate("Dialog", "释义"))
        self.sentenceCheckBox.setText(_translate("Dialog", "例句"))
        self.phraseCheckBox.setText(_translate("Dialog", "短语"))
        self.AmEPhoneticCheckBox.setText(_translate("Dialog", "美式英标"))
        self.noPronRadioButton.setText(_translate("Dialog", "无发音"))
        self.AmEPronRadioButton.setText(_translate("Dialog", "美式发音"))
        self.BrEPronRadioButton.setText(_translate("Dialog", "英式发音"))
        self.credentialGroupBox.setTitle(_translate("Dialog", "账号设置"))
        self.currentDictionaryLabel.setText(_translate("Dialog", "当前选择词典: "))
        self.usernameLabel.setText(_translate("Dialog", "账号"))
        self.passwordLabel.setText(_translate("Dialog", "密码"))
        self.cookieLabel.setText(_translate("Dialog", "Cookie"))
        self.cookieLineEdit.setPlaceholderText(_translate("Dialog", "选填"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("Dialog", "设置"))
        self.dangerZoneGroupBox.setTitle(_translate("Dialog", "Danger Zone"))
        self.btnBackwardTemplate.setToolTip(_translate("Dialog", "Add or Delete Backward Template. (This would affect all cards in current deck)"))
        self.btnBackwardTemplate.setText(_translate("Dialog", "Add/Delete Backward Template"))
        self.utilitiesGroupBox.setTitle(_translate("Dialog", "Utilities"))
        self.btnDownloadMissingAssets.setToolTip(_translate("Dialog", "Check words in selected deck and download missing assets (images, audio files, etc.)"))
        self.btnDownloadMissingAssets.setText(_translate("Dialog", "Download Missing Assets"))
        self.btnExportAudio.setToolTip(_translate("Dialog", "Export all words in selected deck into a single audio file. (macOS only)"))
        self.btnExportAudio.setText(_translate("Dialog", "Export Audio (macOS only)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.utilitiesTab), _translate("Dialog", "工具"))
