install:
	python3 -m venv env; \
	env/bin/pip install --upgrade pip; \
	env/bin/pip install -Ue .; \

clean:
	rm -rf env
