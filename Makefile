all: python

python:
	protoc -Iproto/ --python_out=python/ proto/kegbot/api/*proto

clean:
	rm -rf build dist
	find . -name "*.pyc" | xargs rm -f

.PHONY: clean all python


# vim: noet
