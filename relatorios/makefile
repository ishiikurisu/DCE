default: compile

plot:
	python figs/rel$(R)/main.py
	mv *.png figs/rel$(R)

compile:
	pdflatex prerel$(R).tex
	mv prerel$(R).pdf 130070629.pdf

clean:
	rm *.aux
	rm *.log
