setup:
	python3 -m venv ~/.Game

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	hadolint Dockerfile 
	pylint --disable=R,C,W1203 game.py

all: install lint test