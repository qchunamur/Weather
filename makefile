#macros
PYTHON = python3
PYUIC = pyuic5

#rules
.PHONY: clean
clean:
	find . -name *.pyc -type f -delete
	find . -name __pycache__ -type d -delete

.PHONY: test
test:
	$(PYTHON) -m unittest

.PHONY: run
run:
	$(PYTHON) main.py

.PHONY: uiToPy
uiToPy:
	$(PYUIC) -x source/view/ui/weather.ui -o source/view/weatherUi.py