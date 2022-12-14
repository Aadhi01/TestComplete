from Generic import *
from ToolbarMapping import *
from FindEnum import *

APPLICATION_NAME = "Notepad++"

def ClickToolbarItem(ItemIndex):
  Aliases.Notepad.Toolbar.ClickItem(ItemIndex)
  
def CloseAllActiveWindows():
  ClickToolbarItem(CloseAll)
  Delay(1000)
  if(Aliases.Notepad.DlgSave.Exists):
    Aliases.Notepad.DlgSave.btnNoToAll.Click()
    
def LaunchNotepad():
  launchApplication(APPLICATION_NAME)

def SetTextToActiveEditor(txt):
  Aliases.Notepad.ActiveEditor.Keys(txt)
  
def FindText(txt):
  SetTextToActiveEditor("^F")
  Aliases.Notepad.DlgFind.Body.ClickTab(Find)
  Aliases.Notepad.DlgFind.FindTxt.SetText(txt)
  Aliases.Notepad.DlgFind.btnFind.Click()

def FindMultiple(txt):
  FindText(txt)
  Aliases.Notepad.DlgFind.Close()
  for counter in range(4):
    Delay(1000)
    SetTextToActiveEditor("[F3]")
  