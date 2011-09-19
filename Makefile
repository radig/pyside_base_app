compile:
	pyside-uic -o views/ui_window.py resources/ui/MainWindow.ui
	pyside-uic -o views/ui_dialog.py resources/ui/Dialog.ui
	pyside-rcc -o views/icons_rc.py resources/icons.qrc

clean:
	rm -rf views/ui_window.py views/ui_dialog.py
	rm -rf views/icons_rc.py
	rm -rf *.pyc views/*.pyc models/*.pyc controllers/*.pyc db/*.pyc

run: views/icons_rc.py views/ui_window.py main.py
	python main.py