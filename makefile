make:
	g++ .\kPowerpoint.cpp icon.out.o -o .\kPowerpoint.exe -w
pymake:
	pyinstaller.exe -w .\messageBox.py -i .\ppticon.ico
