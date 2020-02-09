import os, sys, glob

## 1) Filter 

def Filter():
	for sFiles in glob.glob("./5.PeakCalling/*_region.bed"):
		print(sFiles)
		FileName = os.path.split(sFiles)[1]
		Filteredfile = "./6.Filter_PeakRegion/"+FileName.replace(".bed",".filtered.bed")
		cmd = 'awk -F "\\t" "{{ if(\$3 >= \$2) {{ print }}}}" %s > %s'%(sFiles,Filteredfile)
		print(cmd)
		os.system(cmd)
	
#Filter()	

## 2) Take intersecting peaks 

def MergeBed(Re1,Re2,OutfileName):
	ReFile1 = "./6.Filter_PeakRegion/"+Re1+"_peaks_narrow_region.filtered.bed"
	ReFile2 = "./6.Filter_PeakRegion/"+Re2+"_peaks_narrow_region.filtered.bed"
	OutFile = "./6.Filter_PeakRegion/"+OutfileName+"_peaks_narrow_region.filtered.bed"
	cmd = "cat %s %s | bedtools sort -i - | bedtools \
    merge -d 25 -c 4,5 -o collapse -i - | bedtools sort -i - > %s"%(ReFile1,ReFile2,OutFile)
	print(cmd)
	os.system(cmd)

MergeBed("sorghum_V2_leaf_rep1_H3K4me3_S15_R1_001","sorghum_V2_leaf_rep2_H3K4me3_S5_R1_001","Combined_H3K4me3") 
MergeBed("sorghum_V2_leaf_rep1_H3K56ac_S12_R1_001","sorghum_V2_leaf_rep2_H3K56ac_S15_R1_001","Combined_H3K56ac")
