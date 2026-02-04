import sys
from pathlib import Path
import sys
from pathlib import Path
sys.path.insert(0, r"d:\3rd semester project DNA")

from flask import Flask,render_template,request
from algorithms.kmp import kmp_search
from algorithms.suffix_array import build_suffix_array,suffix_search
from algorithms.mutation import detect_mutations
from algorithms.alignment import needleman_wunsch
from ml.mutation_predictor import predict_mutation_probability
from utils.plotter import plot_mutations
from utils.fasta_reader import read_fasta
import io,base64

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    result=None; img=None
    if request.method=="POST":
        dna=request.form.get("dna","")
        if "fasta" in request.files and request.files["fasta"].filename:
            dna=read_fasta(request.files["fasta"])

        pat=request.form["pattern"]

        mut=detect_mutations(dna,pat)
        fig=plot_mutations(mut,len(dna))
        buf=io.BytesIO(); fig.savefig(buf,format="png")
        img=base64.b64encode(buf.getvalue()).decode()

        result={
            "kmp":len(kmp_search(dna,pat)),
            "suffix":len(suffix_search(dna,pat,build_suffix_array(dna))),
            "score":needleman_wunsch(dna,pat),
            "prob":predict_mutation_probability(len(mut), len(dna)),  # ← FIXED: Added len(dna)
            "mut_count": len(mut)
        }

    return render_template("index.html",result=result,img=img)

app.run(debug=True)