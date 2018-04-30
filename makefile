.PHONY: install

install:
	python3 -m venv env; \
	env/bin/pip install --upgrade pip; \
	env/bin/pip install -Ue .; \

clean:
	rm -rf env picamera.egg-info

test:
	env/bin/python -m unittest discover -v picamera/tests/*

install-travis:
	make install

test-travis:
	python -m unittest discover -v picamera/tests/*
