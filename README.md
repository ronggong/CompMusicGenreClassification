# CompMusicGenreClassification
Classifier Jingju, indian, turkish music by machine learning

## Dependencies
pycompmusic: https://github.com/MTG/pycompmusic
essentia: https://github.com/MTG/essentia
gaia2: https://github.com/MTG/gaia

## Use
In main.py  

change '/Users/gong/Documents/Library/gaia-master/src/bindings/pygaia/scripts/classification' path to your gaia correspondent src/bindings/pygaia/scripts/classification path  

change outputFolder to a folder where you want to output the results  

change jingjuFolder to your jingju audio file folder. The structure of this folder is jingjuFolder/artistFolder/audiofile  

python main.py

## Parameters
change classification_project_template.yaml in gaia's classification folder to modify the features and svm parameters

## Output
similarity matrix result will be the .html file in output folder.  
