
with open("data-merge.csv", "w") as o:
    o.write("name, conf, dft@mm, pm7@mm, mm@mm, dft@PM7, pm7@pm7, mmff@pm7, dft@dft, pm7@dft, mmff@dft\n")

    # read the multi-line file
    with open('data-nan.csv') as f:
        f.readline() # header
        while True:
            line1 = f.readline().rstrip()
            line2 = f.readline().rstrip()
            if not line2: break
            line3 = f.readline().rstrip()
            if not line3: break # EOF

            if "error" in line3:
                continue # DFT didn't complete

            # we now have all the data
            mol = line1.split(",")[0]
            conf = line1.split(",")[1][:-5] # remove "-mmff"
            # tokens 1 and 2 are molecule and conformer
            dftMM,pm7MM, mmMM = line1.split(",")[2:5]
            dftPM7,pm7PM7, mmPM7 = line2.split(",")[2:5]
            dftDFT, pm7DFT, mmDFT = line3.split(",")[2:5]
            outLine = ",".join([mol, conf, dftMM, pm7MM, mmMM, dftPM7, pm7PM7, mmPM7, dftDFT, pm7DFT, mmDFT])
            outLine += "\n"
            o.write(outLine)
