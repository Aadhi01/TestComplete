def launchApplication(applicationName):
  Log.Message("Starting application - " + applicationName)
  WshShell.Run(applicationName)
  Log.Message("Application Started!!")
  