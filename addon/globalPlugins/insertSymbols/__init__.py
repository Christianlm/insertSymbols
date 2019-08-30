# -*- coding: UTF-8 -*-

#Copyright (C) 2019 Chris Leo
# Released under GPL 2
# insertSymbols 0.2.0 py3 add-on for NVDA

import globalPluginHandler
import api
import ui
import gui
#from gui import guiHelper
import wx
import addonHandler
addonHandler.initTranslation()
from .  symbolsCategories import categoriesNames, mathematical, smileys, people, activity, animalsAndNature, foodAndDrink, travelAndPlaces, objects, symbols, flags, hands
import scriptHandler
from scriptHandler import script
from globalCommands import SCRCAT_TOOLS

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

	def onInsertSymbols(self, evt):
		gui.mainFrame._popupSettingsDialog(HomePanel)
	@script(
		# Translators: Message presented in input help mode.
		description=_("Open a dialog with available symbols."),
		category = SCRCAT_TOOLS,
		gesture="kb:NVDA+x"
	)
	def script_insertSymbols(self, gesture):
		self.onInsertSymbols(None)
# Function to copy in clipboard:
def to_copySymbols(evt):
	y = evt.GetEventObject().GetName()
	if api.copyToClip(y):
		# Translators: This is the message when the symbol has been copied on  clipboard.
		wx.CallLater(100, ui.message, _("{sbl} Copied in clipboard.").format(sbl=y))
	else:
		wx.CallLater(100, ui.message, _("Cannot copy."))

# A wx.Frame  to choose symbols categories from a menuBar:
class HomePanel(wx.Frame):

	_instance = None
	def __new__ (cls, *args, **kwargs):
		if HomePanel._instance is None:
			return super (HomePanel, cls).__new__(cls, *args, **kwargs)
		return HomePanel._instance

	def __init__(self, parent, *a, **k):
		if HomePanel._instance is not None:
			return
		HomePanel._instance = self

		# Translators: title of the main frame:
		super(HomePanel, self).__init__(parent=parent, title=_("Insert Symbols"))

		menubar = wx.MenuBar()
		mymenu = wx.Menu()
		item1 = mymenu.Append(-1,categoriesNames[0])
		item2 = mymenu.Append(-1, categoriesNames[1])
		item3 = mymenu.Append(-1, categoriesNames[2])
		item4 = mymenu.Append(-1, categoriesNames[3])
		item5 = mymenu.Append(-1, categoriesNames[4])
		item6 = mymenu.Append(-1, categoriesNames[5])
		item7 = mymenu.Append(-1, categoriesNames[6])
		item8 = mymenu.Append(-1, categoriesNames[7])
		item9 = mymenu.Append(-1, categoriesNames[8])
		item10 = mymenu.Append(-1, categoriesNames[9])
		item11 = mymenu.Append(-1, categoriesNames[10])
		item12 = mymenu.Append(-1, _("Exit...\tEsc"))
		# Translators: name of the menu.
		menubar.Append(mymenu, _("Category "))
		self.SetMenuBar(menubar)

		p = wx.Panel(id=wx.NewId(), name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(500, 500), style=wx.TAB_TRAVERSAL)
		t= wx.StaticText(p, -1, _("Welcome on Insert Symbols!\nChoose a category from menu.\nEnjoy!"))
		t.SetFocus()
		closeButton = wx.Button(p, wx.ID_CLOSE)
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
		self.Bind(wx.EVT_CLOSE, self.onClose)

		# Events menu:
		self.Bind(wx.EVT_MENU, self.on_clic_item1, item1)
		self.Bind(wx.EVT_MENU, self.on_clic_item2, item2)
		self.Bind(wx.EVT_MENU, self.on_clic_item3, item3)
		self.Bind(wx.EVT_MENU, self.on_clic_item4, item4)
		self.Bind(wx.EVT_MENU, self.on_clic_item5, item5)
		self.Bind(wx.EVT_MENU, self.on_clic_item6, item6)
		self.Bind(wx.EVT_MENU, self.on_clic_item7, item7)
		self.Bind(wx.EVT_MENU, self.on_clic_item8, item8)
		self.Bind(wx.EVT_MENU, self.on_clic_item9, item9)
		self.Bind(wx.EVT_MENU, self.on_clic_item10, item10)
		self.Bind(wx.EVT_MENU, self.on_clic_item11, item11)
		self.Bind(wx.EVT_MENU, self.on_clic_item12, item12)

	# Callbacks menu:
	def on_clic_item1(self, evt): gui.mainFrame._popupSettingsDialog(MathematicalDialog)
	def on_clic_item2(self, evt): gui.mainFrame._popupSettingsDialog(SmileysDialog)
	def on_clic_item3(self, evt): gui.mainFrame._popupSettingsDialog(PeopleDialog)
	def on_clic_item4(self, evt): gui.mainFrame._popupSettingsDialog(ActivityDialog)
	def on_clic_item5(self, evt): gui.mainFrame._popupSettingsDialog(AnimalsAndNatureDialog)
	def on_clic_item6(self, evt): gui.mainFrame._popupSettingsDialog(FoodAndDrinkDialog)
	def on_clic_item7(self, evt): gui.mainFrame._popupSettingsDialog(TravelAndPlacesDialog)
	def on_clic_item8(self, evt): gui.mainFrame._popupSettingsDialog(ObjectsDialog)
	def on_clic_item9(self, evt): gui.mainFrame._popupSettingsDialog(SymbolsDialog)
	def on_clic_item10(self, evt): gui.mainFrame._popupSettingsDialog(FlagsDialog)
	def on_clic_item11(self, evt): gui.mainFrame._popupSettingsDialog(HandsDialog)
	def on_clic_item12(self, evt):
		self.Destroy()
		HomePanel._instance = None

	def onClose(self, evt):
		self.Destroy()
		HomePanel._instance = None

	def __del__ (self):
		HomePanel._instance = None

# Classes for each categories (from  0 to 10):
class MathematicalDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if MathematicalDialog._instance is None:
			return super (MathematicalDialog, cls).__new__(cls, *args, **kwargs)
		return MathematicalDialog._instance

	def __init__(self, parent, *a, **k):
		if MathematicalDialog._instance is not None:
			return
		MathematicalDialog._instance = self

		super(MathematicalDialog, self).__init__(parent=parent, title=categoriesNames[0])
		#from symbolsCategories import mathematical 
		li = mathematical
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL)
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		MathematicalDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		MathematicalDialog._instance = None

	def __del__ (self):
		MathematicalDialog._instance = None

class SmileysDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if SmileysDialog._instance is None:
			return super (SmileysDialog, cls).__new__(cls, *args, **kwargs)
		return SmileysDialog._instance

	def __init__(self, parent, *a, **k):
		if SmileysDialog._instance is not None:
			return
		SmileysDialog._instance = self

		super(SmileysDialog, self).__init__(parent=parent, title=categoriesNames[1])
		#from symbolsCategories import smileys 
		li = smileys
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL)
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		#s.Add(wx.Button(self, wx.ID_CANCEL, _("Cancel")), 1, wx.EXPAND|wx.ALL, 5)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		SmileysDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		SmileysDialog._instance = None

	def __del__ (self):
		SmileysDialog._instance = None

class PeopleDialog(wx.Dialog):

	_instance = None
	def __new__ (cls, *args, **kwargs):
		if PeopleDialog._instance is None:
			return super (PeopleDialog, cls).__new__(cls, *args, **kwargs)
		return PeopleDialog._instance

	def __init__(self, parent, *a, **k):
		if PeopleDialog._instance is not None:
			return
		PeopleDialog._instance = self

		super(PeopleDialog, self).__init__(parent=parent, title=categoriesNames[2])

		#from symbolsCategories import people 
		li = people
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)

		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL)
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)

		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		PeopleDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		PeopleDialog._instance = None

	def __del__ (self):
		PeopleDialog._instance = None

class ActivityDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if ActivityDialog._instance is None:
			return super (ActivityDialog, cls).__new__(cls, *args, **kwargs)
		return ActivityDialog._instance

	def __init__(self, parent, *a, **k):
		if ActivityDialog._instance is not None:
			return
		ActivityDialog._instance = self

		super(ActivityDialog, self).__init__(parent=parent, title=categoriesNames[3])
		#from symbolsCategories import activity 
		li = activity
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL)
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		ActivityDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		ActivityDialog._instance = None

	def __del__ (self):
		ActivityDialog._instance = None

class AnimalsAndNatureDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if AnimalsAndNatureDialog._instance is None:
			return super (AnimalsAndNatureDialog, cls).__new__(cls, *args, **kwargs)
		return AnimalsAndNatureDialog._instance

	def __init__(self, parent, *a, **k):
		if AnimalsAndNatureDialog._instance is not None:
			return
		AnimalsAndNatureDialog._instance = self

		super(AnimalsAndNatureDialog, self).__init__(parent=parent, title=categoriesNames[4])
		#from symbolsCategories import animalsAndNature 
		li = animalsAndNature
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		AnimalsAndNatureDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		AnimalsAndNatureDialog._instance = None

	def __del__ (self):
		AnimalsAndNatureDialog._instance = None

class FoodAndDrinkDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if FoodAndDrinkDialog._instance is None:
			return super (FoodAndDrinkDialog, cls).__new__(cls, *args, **kwargs)
		return FoodAndDrinkDialog._instance

	def __init__(self, parent, *a, **k):
		if FoodAndDrinkDialog._instance is not None:
			return
		FoodAndDrinkDialog._instance = self

		super(FoodAndDrinkDialog, self).__init__(parent=parent, title=categoriesNames[5])
		#from symbolsCategories import foodAndDrink 
		li = foodAndDrink
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		FoodAndDrinkDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		FoodAndDrinkDialog._instance = None

	def __del__ (self):
		FoodAndDrinkDialog._instance = None

class TravelAndPlacesDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if TravelAndPlacesDialog._instance is None:
			return super (TravelAndPlacesDialog, cls).__new__(cls, *args, **kwargs)
		return TravelAndPlacesDialog._instance

	def __init__(self, parent, *a, **k):
		if TravelAndPlacesDialog._instance is not None:
			return
		TravelAndPlacesDialog._instance = self

		super(TravelAndPlacesDialog, self).__init__(parent=parent, title=categoriesNames[6])
		#from symbolsCategories import travelAndPlaces 
		li = travelAndPlaces
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		TravelAndPlacesDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		TravelAndPlacesDialog._instance = None

	def __del__ (self):
		TravelAndPlacesDialog._instance = None

class ObjectsDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if ObjectsDialog._instance is None:
			return super (ObjectsDialog, cls).__new__(cls, *args, **kwargs)
		return ObjectsDialog._instance

	def __init__(self, parent, *a, **k):
		if ObjectsDialog._instance is not None:
			return
		ObjectsDialog._instance = self

		super(ObjectsDialog, self).__init__(parent=parent, title=categoriesNames[7])
		#from symbolsCategories import objects 
		li = objects
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		ObjectsDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		ObjectsDialog._instance = None

	def __del__ (self):
		ObjectsDialog._instance = None

class SymbolsDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if SymbolsDialog._instance is None:
			return super (SymbolsDialog, cls).__new__(cls, *args, **kwargs)
		return SymbolsDialog._instance

	def __init__(self, parent, *a, **k):
		if SymbolsDialog._instance is not None:
			return
		SymbolsDialog._instance = self

		super(SymbolsDialog, self).__init__(parent=parent, title=categoriesNames[8])
		#from symbolsCategories import symbols 
		li = symbols
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		SymbolsDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		SymbolsDialog._instance = None

	def __del__ (self):
		SymbolsDialog._instance = None

class FlagsDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if FlagsDialog._instance is None:
			return super (FlagsDialog, cls).__new__(cls, *args, **kwargs)
		return FlagsDialog._instance

	def __init__(self, parent, *a, **k):
		if FlagsDialog._instance is not None:
			return
		FlagsDialog._instance = self

		super(FlagsDialog, self).__init__(parent=parent, title=categoriesNames[9])
		#from symbolsCategories import flags 
		li = flags
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		FlagsDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		FlagsDialog._instance = None

	def __del__ (self):
		FlagsDialog._instance = None

class HandsDialog(wx.Dialog):
	_instance = None
	def __new__ (cls, *args, **kwargs):
		if HandsDialog._instance is None:
			return super (HandsDialog, cls).__new__(cls, *args, **kwargs)
		return HandsDialog._instance

	def __init__(self, parent, *a, **k):
		if HandsDialog._instance is not None:
			return
		HandsDialog._instance = self

		super(HandsDialog, self).__init__(parent=parent, title=categoriesNames[10])
		#from symbolsCategories import hands 
		li = hands
		for symb in li:
			b = wx.Button(self, -1, symb, size=(50, 30), name=symb)
			b.Bind(wx.EVT_BUTTON, self.on_clic)
		s = wx.BoxSizer()
		cancelButton = wx.Button(self, wx.ID_CANCEL) #_("&Cancel"))
		s.Add(cancelButton, wx.ID_CANCEL)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		s1 = wx.BoxSizer(wx.VERTICAL)
		s1.Add(b, -1)
		s1.Add(s, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(s1)
		s1.Fit(self)

	def on_clic(self,evt):
		to_copySymbols(evt)
		self.Destroy()
		HandsDialog._instance = None

	def onCancel(self, evt):
		self.Destroy()
		HandsDialog._instance = None

	def __del__ (self):
		HandsDialog._instance = None
