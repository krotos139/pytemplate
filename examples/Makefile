.SUFFIXES: .tex .pdf .dot .png
GENERATOR=../pytemplate.py
TEX=out_doc1.pdf
DIGRAPH=
GENFILES=out_doc1_part1.tex out_doc1_part2.tex out_doc1_part3.tex out_doc1_part4.tex out_doc1_part5.tex out_doc2_ready.odt

all: $(GENFILES) $(DIGRAPH) $(TEX) output

out_doc1_part1.tex:
	$(GENERATOR) -t out_doc1_part1.template.tex -o out_doc1_part1.tex

out_doc1_part2.tex:
	$(GENERATOR) -t out_doc1_part2.template.tex -o out_doc1_part2.tex

out_doc1_part3.tex:
	$(GENERATOR) -t out_doc1_part3.template.tex -o out_doc1_part3.tex

out_doc1_part4.tex:
	$(GENERATOR) -t out_doc1_part4.template.tex -o out_doc1_part4.tex

out_doc1_part5.tex:
	$(GENERATOR) -t out_doc1_part5.template.tex -o out_doc1_part5.tex

out_doc2_ready.odt:
	$(GENERATOR) -f odt -t out_doc2.odt -o out_doc2_ready.odt


output:
	mkdir output
	cp out_doc1.pdf output
	cp out_doc2_ready.odt output

clean:
	rm -f *.pdf
	rm -rf output
	rm -f $(GENFILES)

.tex.pdf:
	pdflatex $<
	pdflatex $<

.dot.png:
	dot -Tpng $< -o$@
	mv -f $@ ./img/
	

